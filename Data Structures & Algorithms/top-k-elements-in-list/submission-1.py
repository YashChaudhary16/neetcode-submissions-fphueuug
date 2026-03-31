class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = {}
        res = []

        for number in nums:
            count_dict[number] = count_dict.get(number, 0) + 1

        sorted_array = sorted(count_dict.items(), key = lambda x: x[1], reverse=True)[:k]

        for item in sorted_array:
            res.append(item[0])

        return res