class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):

            difference = target - numbers[i]

            start = i + 1
            end = len(numbers) - 1

            while start <= end:
                mid = (start + end)//2

                if numbers[mid] < difference:
                    start = mid + 1
                if numbers[mid] > difference:
                    end = mid - 1
                if numbers[mid] == difference:
                    return [i+1, mid+1]
                    
                