class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = []

        for token in tokens:
            if res:
                if token == "+":
                    res.append(res[-1] + res[-2])
                    res.pop(-2)
                    res.pop(-2)
                elif token == "*":
                    res.append(res[-1] * res[-2])
                    res.pop(-2)
                    res.pop(-2)
                    print(res)
                elif token == "-":
                    res.append(res[-2] - res[-1])
                    res.pop(-2)
                    res.pop(-2)
                elif token == "/":
                    result = res[-2] / res[-1]
                    if result < 0:
                        res.append(math.ceil(result))
                    else:
                        res.append(math.floor(result))
                    res.pop(-2)
                    res.pop(-2)
                else:
                    res.append(int(token))
            else:
                res.append(int(token))

        return res[-1]