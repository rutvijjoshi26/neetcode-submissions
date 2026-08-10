class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}

        for i, n in enumerate(nums):
            temp = target - n
            if temp in H:
                if H[temp] != i:
                    return [H[temp], i]
            else:
                H[n] = i
            