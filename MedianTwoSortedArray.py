#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

def findMedianSortedArray(nums1,nums2):
    nums1 += nums2
    nums1=sorted(nums1)
    if len(nums1) % 2 == 1:
        print('here')
        return nums1[len(nums1)//2]
    return (nums1[len(nums1)//2-1] + nums1[len(nums1)//2])/2
print(findMedianSortedArray([],[2,3]))
