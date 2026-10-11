class KthLargest:

    k: int
    kth_largest: List[int]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kth_largest = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if len(self.kth_largest) == 0:
            self.kth_largest.append(val)
            return val

        if len(self.kth_largest) < self.k:
            self.kth_largest.append(val)

        elif val > self.kth_largest[-1]:
            self.kth_largest[-1] = val

        i = len(self.kth_largest) - 2

        while i >= 0 and self.kth_largest[i] < self.kth_largest[i + 1]:
            self.kth_largest[i], self.kth_largest[i + 1] = self.kth_largest[i + 1], self.kth_largest[i]
            i -= 1

        return self.kth_largest[-1]
