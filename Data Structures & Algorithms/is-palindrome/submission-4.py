class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_string = []

        for char in s:
            if (ord(char.lower()) >= 97 and ord(char.lower()) <= 122):
                filtered_string.append(char.lower())
            if ord(char) >= 48 and ord(char) <= 57:
                filtered_string.append(char)
        
        string = ''.join(filtered_string)

        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False
            left+=1
            right-=1

        return True