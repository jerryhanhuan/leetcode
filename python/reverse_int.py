#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:reverse_int.py
#Created Time:2019-08-05 04:25:00


# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
# 例如， 输入 123 => 输出 321，输入 123, 输出 -321, 输入 120 ，输出 21





class Solution:
    # def reverse(self, x:int) -> int:
    def reverse(self, x):
        postive = 0
        if x > 0:
            postive = 1
        elif x == 0:
            return 0
        else:
            x = abs(x)
            postive = 0
        s = str(x)
        s1 = ''
        for i in range(len(s)):
            s1+=s[len(s)-1-i]
        n = int(s1)
        if postive == 0:
            n = -n
        if n < -(2**31):
            return 0
        elif n > (2**31 - 1):
            return 0
        return n


if __name__ == '__main__':
    s = int(input('请输入一个整数::'))
    ro = Solution()
    n = ro.reverse(s)
    print(n)
