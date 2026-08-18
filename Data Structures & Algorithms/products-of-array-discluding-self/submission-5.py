class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                count += 1
        res = []
        if count > 1:
            return [0] * len(nums)
        for num in nums:
            if count > 0:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
            else:
                res.append(int(product/num))
        return res