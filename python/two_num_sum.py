#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:two_num_sum.py
#Created Time:2019-07-22 01:48:52

'''
两数之和：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案，但是，你不能重复利用这个数组中同样的元素。

示例:
    给定  nums = [2,7,11,15],target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0,1]


'''

'''
# 两层 for 循环，遍历

class Solution(object):
    
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []



if __name__ == '__main__':
    nums = [i for i in range(1,1000)]
    target = 200
    s = Solution()
    result = s.twoSum(nums, target)
    print('result:', result)
    print('%d + %d = %d'%(nums[result[0]], nums[result[1]], target))
    

'''


class Solution(object):
    def twoSum(self,nums,target):
        index = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in index:
                return [i,index[diff]]
            index[n] = i
        return []

if __name__ == '__main__':
    nums = [i for i in range(1,1000000)]
    target = 192736
    s = Solution()
    result = s.twoSum(nums,target)
    print('result:', result)
    print('%d + %d = %d'%(nums[result[0]], nums[result[1]], target))


