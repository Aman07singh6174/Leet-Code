class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maximum = max(nums)
        return sum(maximum - i for i in nums)