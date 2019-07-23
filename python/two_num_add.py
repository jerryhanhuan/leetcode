#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:two_num_add.py
#Created Time:2019-07-23 01:08:16


'''
问题描述：
给出两个 非空 的链表用来表示两个非负的整数，其中，它们各自的位数是按照 逆序的方式存储的，
并且它们的每个节点都只能存储 一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
可以假设 除了数字0之外，这两个数都不会以 0 开头

示例：

输入：
(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 ->8
原因： 342 + 465 = 807

方法1： 将 l1 和 l2 分别转换为数值，然后求和，再将其转换为 ListNode

'''

'''
# 方法一
# 将 l1 和  l2 分别转为数值，然后求和，再将其转换为 ListNode

from functools import reduce

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # ListNode -> Num 
    def List2Num(self,l):
        l_n = []
        while l != None:
            l_n.append(l.val)
            l = l.next
        l_n.reverse()
        return reduce(lambda x,y:x*10+y,l_n)

    # Num -> ListNode
    def Num2List(self,num):
        l_n = list(map(int,str(num)))
        l_n.reverse()
        head = ListNode(l_n[0])
        l = head
        for i in range(1,len(l_n)):
            l.next = ListNode(l_n[i])
            l = l.next
        return head

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        num_l1 = self.List2Num(l1)
        num_l2 = self.List2Num(l2)
        sum = num_l1 + num_l2
        l_sum = ListNode(0)
        l_sum = self.Num2List(sum)
        return l_sum

''' 

# 方法2，逐位相加，有进位，则下一组和+1


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None



class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        p = head
        tempsum = 0
        while True:
            if l1 is not None:
                tempsum += l1.val
                l1 = l1.next
            if l2 is not None:
                tempsum += l2.val
                l2 = l2.next
            p.val = tempsum % 10
            tempsum = tempsum // 10
            if l1 is None and l2 is None and tempsum == 0:
                break
            p.next = ListNode(0)
            p = p.next
        return head






if __name__ == '__main__':

    n1,n2,n3,m1,m2,m3 = ListNode(0),ListNode(0),ListNode(0),ListNode(0),ListNode(0),ListNode(0)
    n1.val = 2
    n1.next = n2
    n2.val = 4
    n2.next = n3
    n3.val = 3
    n3.next = None
    
    m1.val = 5
    m1.next = m2
    m2.val = 6
    m2.next = m3
    m3.val = 4
    m3.next = None

    s = Solution()
    sum = ListNode(0)
    sum = s.addTwoNumbers(n1,m1) 
    while True:
        print(sum.val)
        if sum.next == None:
            break
        else:
            sum = sum.next










