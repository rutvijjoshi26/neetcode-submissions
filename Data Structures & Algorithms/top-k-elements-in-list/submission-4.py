class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return list(freq)[:k]
        
