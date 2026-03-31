class Solution:
    def isValid(self, s: str) -> bool:

        res = []

        for i in range(len(s)):
            if len(res) != 0:
                if (s[i] == '}' and res[-1] == '{') or (s[i] == ']' and res[-1] == '[') or (s[i] == ')' and res[-1] == '('):
                    res.remove(res[-1])
                else:
                    res.append(s[i])
            else:
                res.append(s[i])

        print(res)

        return len(res) == 0


        

        