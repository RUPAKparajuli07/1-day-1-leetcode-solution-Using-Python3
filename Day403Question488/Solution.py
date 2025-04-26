class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        # Function to remove continuous balls (3 or more) of the same color starting from index i
        def remove_same(s, i):
            if i < 0:
                return s  # If index is invalid, return the string as is

            # Initialize left and right pointers to i
            left = right = i
            
            # Move left pointer to the start of same-colored sequence
            while left > 0 and s[left-1] == s[i]:
                left -= 1
            
            # Move right pointer to the end of same-colored sequence
            while right+1 < len(s) and s[right+1] == s[i]:
                right += 1

            # Calculate the length of the same-colored sequence
            length = right - left + 1
            
            # If 3 or more balls are same, remove them and recursively check again
            if length >= 3:
                new_s = s[:left] + s[right+1:]  # Remove the sequence
                return remove_same(new_s, left-1)  # Recursively remove further possible groups
            else:
                return s  # If less than 3, no removal happens

        # Sort the hand to handle same colored balls together
        hand = "".join(sorted(hand))

        # Initialize BFS queue with (board, hand, steps)
        q = collections.deque([(board, hand, 0)])

        # Set to keep track of visited states (to avoid repeating)
        visited = set([(board, hand)])

        # Start BFS
        while q:
            curr_board, curr_hand, step = q.popleft()

            # Try inserting each ball in hand at every position in the board
            for i in range(len(curr_board)+1):
                for j in range(len(curr_hand)):
                    
                    # Skip if this hand ball is same as previous one (to avoid duplicates)
                    if j > 0 and curr_hand[j] == curr_hand[j-1]:
                        continue

                    # Only insert at the beginning of a group of same-colored balls
                    if i > 0 and curr_board[i-1] == curr_hand[j]:  # Left of position is same color
                        continue

                    pick = False  # Flag to check if insertion is meaningful

                    # Case 1: If ball matches the one at current position
                    if i < len(curr_board) and curr_board[i] == curr_hand[j]:
                        pick = True
                    
                    # Case 2: If left and right of position are same but not equal to the ball being inserted
                    if 0 < i < len(curr_board) and curr_board[i-1] == curr_board[i] and curr_board[i] != curr_hand[j]:
                        pick = True

                    # If this position is valid for insertion
                    if pick:
                        # Insert the ball and try to remove same-colored sequences
                        new_board = remove_same(curr_board[:i] + curr_hand[j] + curr_board[i:], i)

                        # Remove used ball from hand
                        new_hand = curr_hand[:j] + curr_hand[j+1:]

                        # If board is empty after removal, return steps + 1
                        if not new_board:
                            return step + 1

                        # If this new state is not visited, add to queue and mark as visited
                        if (new_board, new_hand) not in visited:
                            q.append((new_board, new_hand, step+1))
                            visited.add((new_board, new_hand))

        # If no solution found, return -1
        return -1
