#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:node.py
#Created Time:2019-07-23 05:09:27




class Node:
    def __init__(self,n):
        self.val = n
        self.next = None



def test():
    head = Node(1)
    p = head
    for i in range(2,11):
        p.next = Node(i)
        p = p.next
    return head


if __name__ == '__main__':
    head = test()
    p = head
    while p is not None:
        print(p.val)
        p = p.next

