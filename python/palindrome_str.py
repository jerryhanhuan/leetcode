#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:palindrome_str.py
#Created Time:2019-07-30 01:16:08

# 判断字符串是否是回文字符串


class Solution:
    # 判断字符串是否是回文字符串
    def IsPalindromeStr(self, s):
        s_len = len(s)
        for i in range(0, s_len//2):
            if s[i] != s[s_len-1-i]:
                return False
        return True
    
    # 获取最长的回文子串
    def longestPalindrome(self,s):
        sub = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        max_str = ""
        for i in sub:
            if self.IsPalindromeStr(i):
                if len(i) > len(max_str):
                    max_str = i
        return max_str



if __name__ == '__main__':
    s = input('请输入一个字符串::')
    sopp = Solution()
    if sopp.IsPalindromeStr(s):
        print('%s 是回文字符串'%(s))
    else:
        print('%s 不是回文字符串'%(s))

    sub_palind = sopp.longestPalindrome(s)
    print('最长回文字串:%s'%(sub_palind))




