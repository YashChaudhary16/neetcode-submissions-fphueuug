class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res_dict = {}
        res = [0] * len(temperatures)
        check_stack = []

        for i, temp in enumerate(temperatures):
            if check_stack:
                while check_stack and check_stack[-1][1] < temp:
                    res_dict[check_stack[-1][0]] = i - check_stack[-1][0]
                    check_stack.pop()
                else:
                    check_stack.append([i, temp])
            else:
                check_stack.append([i, temp])

        for i in range(len(temperatures)):
            if i in res_dict:
                res[i] = res_dict[i]

        return res

                
