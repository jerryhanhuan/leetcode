#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:strnum2int.py
#Created Time:2019-08-06 01:25:35


from functools import reduce


INT_MIN = -(2**31)
INT_MAX = 2**31-1
DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7, '8':8, '9':9}


class Solution:
    def filter(self, strnum):
        strnum = strnum.lstrip()
        s = ''
        positive = 0 
        if len(strnum) == 0:
            return (positive,[])
        if strnum[0] == '-':
            positive = 0 
            s = strnum[1:]
        elif strnum[0] == '+':
            positive = 1 
            s = strnum[1:]
        elif strnum[0] < '0' or strnum[0] > '9':
            return (positive,[])
        else:
            positive = 1 
            s = strnum[:]
        num = []
        for n in s:
            if n < '0'or n > '9':
                break
            else:
                num.append(self.char2int(n))
        return positive, num 
    

    def mulifun(self,x,y):
        return x*10 + y 

    def char2int(self,x):
        return DIGITS[x]


    # def myAtoi(self, strnum: str) -> int
    def myAtoi(self, strnum):
        positive,num_list = self.filter(strnum)
        if len(num_list) == 0:
            return 0
        num = reduce(self.mulifun,num_list)
        if  positive == 0:
            num = -num
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num 
        



if __name__ == '__main__':
    s = input('请输入字符串::')
    so = Solution()
    num = so.myAtoi(s)
    print('num is %d'%(num))


