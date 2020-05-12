#Given a string, find the length of the longest substring without repeating characters.


def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        length = 0
        for i in s:
            if i in substring:
                substring = substring[substring.index(i) + 1:]
            substring += i
            if len(substring) > length:
                length = len(substring)
        return length
        