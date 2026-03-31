class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        visited = [False] * len(temperatures)

        for i in range(len(temperatures)):
            left, right = i, i+1
            while right < len(temperatures):
                if temperatures[left] < temperatures[right]:
                    res[left] = right - left
                    visited[left] = True
                    left = right
                    right += 1
                else:
                    right += 1

        return res
