class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s):
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255:
                    return False
                if part != str(int(part)):  # checks for leading zeros
                    return False
            return True

        def isIPv6(s):
            parts = s.split(':')
            if len(parts) != 8:
                return False
            hex_digits = '0123456789abcdefABCDEF'
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return False
                if not all(c in hex_digits for c in part):
                    return False
            return True

        if queryIP.count('.') == 3 and isIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(':') == 7 and isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
