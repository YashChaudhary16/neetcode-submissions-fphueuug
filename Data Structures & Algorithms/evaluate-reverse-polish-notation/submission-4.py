class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = []

        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
                res.append(int(tokens[i]))
                print(res)
            else:
                if tokens[i] == "+":
                    res[-2] = res[-1] + res[-2]
                    res.pop()
                    print(res)
                elif tokens[i] == "-":
                    res[-2] = res[-2] - res[-1]
                    res.pop()
                    print(res)
                elif tokens[i] == "*":
                    res[-2] = res[-1] * res[-2]
                    res.pop()
                    print(res)
                elif tokens[i] == "/":
                    res[-2] = int(res[-2] / res[-1])
                    res.pop()
                    print(res)
        
        return res[0]
        