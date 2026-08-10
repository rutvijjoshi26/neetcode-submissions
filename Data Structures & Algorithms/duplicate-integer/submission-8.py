class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if freq.get(num):
                return True
            else:
                freq[num] = 1
        return False