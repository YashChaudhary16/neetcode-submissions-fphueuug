class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = []

        for token in tokens:
            if res:
                if token == "+":
                    result = int(res[-1]) + int(res[-2])
                    res.pop()
                    res.pop()
                    res.append(str(result))
                    print(res)
                elif token == "*":
                    result = int(res[-1]) * int(res[-2])
                    res.pop()
                    res.pop()
                    res.append(str(result))
                    print(res)
                elif token == "-":
                    result = int(res[-2]) - int(res[-1])
                    res.pop()
                    res.pop()
                    res.append(str(result))
                    print(res)
                elif token == "/":
                    result = int(res[-2]) / int(res[-1])
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                    res.pop()
                    res.pop()
                    res.append(str(result))
                    print(res)
                else:
                    res.append(token)
            else:
                res.append(token)

        return int(res[-1])