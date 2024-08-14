class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        temp = 0
        for i in range(0,len(nums3)-1):
            for j in range(i+1,len(nums3)):
                if nums3[i] > nums3[j]:
                    temp = nums3[i]
                    nums3[i] = nums3[j]
                    nums3[j] = temp
        if len(nums3) % 2 == 1:
            return nums3[len(nums3)//2]
        else:
            return (nums3[len(nums3)//2-1] + nums3[len(nums3)//2])/2
