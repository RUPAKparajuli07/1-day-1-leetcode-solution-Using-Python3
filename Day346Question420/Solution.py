class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # Checking if we have at least one lowercase, uppercase, and digit
        has_lower = has_upper = has_digit = False
        for char in password:
            if char.islower():
                has_lower = True
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True
        
        missing_types = 3 - (has_lower + has_upper + has_digit)
        
        # Finding sequences of three or more repeating characters
        replace = 0  # Number of replacements needed for repeating characters
        one_mod = two_mod = 0  # Counts of sequences of length % 3 == 1 and 2
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                
                replace += length // 3
                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1
            else:
                i += 1
        
        # Case 1: If password is too short
        if n < 6:
            return max(6 - n, missing_types)
        
        # Case 2: If password is within the valid length range
        elif n <= 20:
            return max(replace, missing_types)
        
        # Case 3: If password is too long
        else:
            excess_length = n - 20
            
            # Reduce replace operations by first removing characters from sequences
            replace -= min(excess_length, one_mod * 1) // 1
            replace -= min(max(excess_length - one_mod, 0), two_mod * 2) // 2
            replace -= max(excess_length - one_mod - 2 * two_mod, 0) // 3
            
            return excess_length + max(replace, missing_types)
