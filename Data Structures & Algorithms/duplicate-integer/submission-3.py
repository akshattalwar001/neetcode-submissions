class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = sorted(nums)
        nums2 = sorted(list(set(nums)))
        return nums1 != nums2
        