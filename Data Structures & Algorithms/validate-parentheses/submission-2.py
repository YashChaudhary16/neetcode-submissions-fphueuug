class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for bracket in s:
            if res:
                if (
                    (res[-1] == "[" and bracket == "]") or
                    (res[-1] == "{" and bracket == "}") or
                    (res[-1] == "(" and bracket == ")")
                ):
                    res.pop()
                else:
                    res.append(bracket)
            else:
                res.append(bracket)

        return len(res) == 0
