class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    temp+=1
                    res[i] = temp
                    break
                else:
                    temp+=1

        return res
