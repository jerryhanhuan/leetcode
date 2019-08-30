#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:pow.py
#Created Time:2019-08-30 01:10:55

'''
class Solution:
    #def myPow(self, x: float, n: int) -> float:
    def myPow(self,x,n):
        if n == 0:
            return 1
        elif x < -100.0 or x > 100.0:
            return -1
        elif n <-(2**31) or n > 2**31-1:
            return -1
        if n < 0:
            return 1/(x**abs(n))
        else:
            return x**n
'''

class Solution:
    def myPow(self,x,n):
        if n == 0:
            return 1.0
        elif n < 0:
            x = 1/x
            n = abs(n)
        if n % 2:
            #error,递归深度失败错误
            #return x * self.myPow(x*x,n/2)
            return x * self.myPow(x,n-1)
        else:
            return self.myPow(x*x,n/2)



if __name__ == '__main__':
	x = float(input('请输入一个数::'))
	n = int(input('请输入幂::'))
	s = Solution();
	r = s.myPow(x,n)
	print('result:',r)


