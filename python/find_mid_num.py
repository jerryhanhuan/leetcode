#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:find_mid_num.py
#Created Time:2019-07-25 02:39:28

'''
给定两个大小为 m 和 n 的有序数组 nums1，nums2
找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m+n))

可以假设 nums1 和 nums2 不会同时为空

eg1:

nums1 = [1, 3]
nums2 = [2]
则中位数是: 2.0

示例2:

nums1 = [1,2]
nums2 = [3,4]
则中位数是 (2+3)/2 = 2.5


'''

class Solution:
    #def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findMedianSortedArrays(self, nums1, nums2):
            L = []
            #  for item in nums1:
            #      L.append(item)
            #  for item in nums2:
            #      L.append(item)
            #  L.sort()
            L = sorted(nums1+nums2)
            if len(L) % 2:
                return L[ (len(L)-1)//2]/1
            else:
                return (L[(len(L)//2 -1)] + L[ len(L)//2] )/2


if __name__ == '__main__':
    num1 = [1,3]
    num2 = [2]

    s = Solution();
    r1 = s.findMedianSortedArrays(num1, num2)
    print('r1:', r1)

    num3 = [1,2]
    num4 = [3,4]
    r2 = s.findMedianSortedArrays(num3, num4)
    print('r2:', r2)





