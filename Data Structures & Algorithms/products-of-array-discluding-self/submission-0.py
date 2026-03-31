class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pseudo_product = nums[-1]

        product_array = []
        product = 1  # Start with 1 as the initial product
        for num in nums:
            product *= num  # Multiply the current product by the current element
            product_array.append(product)  # Append the product to the result list

        print(product_array)
        res = [product_array[-2]]

        for i in range(len(nums) - 2, -1, -1):
            if i == 0:
                res.append(pseudo_product)
                break
            res.append(product_array[i-1]*pseudo_product)
            pseudo_product *= nums[i]

        return res[::-1]