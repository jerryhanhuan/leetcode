#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:palindrome_num.py
#Created Time:2019-08-07 00:57:31



class Solution:
	#def isPalindrome(self, x: int) -> bool:
            def isPalindrome(self,x):
                s = str(x)
                for i in range(len(s)//2):
                    if s[i] != s[len(s)-1-i]:
                        return False
                return True


if __name__ == '__main__':
    n = int(input('请输入一个数字::'))
    s = Solution()
    if s.isPalindrome(n):
        print('True')
    else:
        print('False')
