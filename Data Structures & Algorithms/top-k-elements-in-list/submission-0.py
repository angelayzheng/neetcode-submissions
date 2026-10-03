class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_chars = {}

        for n in nums:
            if n in top_chars:
                top_chars[n] += 1
            else:
                top_chars[n] = 1

        top = [(top_chars[c], c) for c in top_chars]
        top.sort(reverse=True)

        return [a[1] for a in top[:k]]