class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = {}
        res = []

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        
        count_dict_sorted = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

        for (item, val) in count_dict_sorted:
            if k:
                res.append(item)
                k-=1
            else:
                return res

        return res

