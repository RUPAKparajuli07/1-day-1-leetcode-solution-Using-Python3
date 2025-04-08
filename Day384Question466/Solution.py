class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not n1:
            return 0

        s1_count = 0  # number of s1 processed
        s2_count = 0  # number of s2 matched
        index = 0     # current index in s2
        recall = dict()  # to detect cycle

        while s1_count < n1:
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2_count += 1
                        index = 0

            s1_count += 1
            # Cycle detection
            if index in recall:
                s1_count_prev, s2_count_prev = recall[index]
                # length of the cycle
                cycle_s1 = s1_count - s1_count_prev
                cycle_s2 = s2_count - s2_count_prev

                # how many full cycles fit
                remaining_s1 = n1 - s1_count
                full_cycles = remaining_s1 // cycle_s1

                s1_count += full_cycles * cycle_s1
                s2_count += full_cycles * cycle_s2
            else:
                recall[index] = (s1_count, s2_count)

        return s2_count // n2
