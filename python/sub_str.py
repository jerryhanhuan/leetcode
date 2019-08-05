#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:sub_str.py
#Created Time:2019-07-24 01:43:15

'''
问题描述
给定一个字符串，请你找出其中不含有重复字符 的 最长字串的长度

示例：
输入： 'abcabcbb'
输出:  3
解析： 因为无重复字符的最长子串是 'abc',所以其长度为 3

输入:  'bbbbb'
输出:   1
解析： 因为无重复字符的最长子串是 'b'，所以其长度为1

'''

'''

class Solution:

    # 是否含有重复字符
    def IsUnique(self, s):
        for i in range(len(s)):
            if s.count(s[i]) != 1:
                return False
        return True

    # def lengthOfLongestSubstring(self, s: str) -> int:
    def lengthOfLongestSubstring(self, s):
        sub_str = list(set(s[i: i+x+1] for x in range(len(s)) for i in range(len(s) - x) ))
        r_str = []
        for i in range(len(sub_str)):
            if self.IsUnique(sub_str[i]):
                r_str.append(sub_str[i])
        max_len = 0
        for i in range(len(r_str)):
            if len(r_str[i]) > max_len:
                max_len = len(r_str[i])
        return max_len
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp = ''
        length = 0
        for i in s:
            if i not in temp:
                temp += i
                length = max(len(temp),length)
            else:
                temp += i
                temp = temp[temp.index(i)+1:]
                print(temp)
        return length


if __name__ == '__main__':
    s = Solution()
    s_str = input('请输入字符串:')
    max_len = s.lengthOfLongestSubstring(s_str)
    print(max_len)

