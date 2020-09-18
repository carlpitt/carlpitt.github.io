# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:53:52 2020

@author: student
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial(n):
    assert n > -1 and type(n) == int
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

def combin(n, r):
    if r > n or r < 0 or n < 0:
        return 0
    if r == 0 or r == n:
        return 1
    return combin(n - 1, r - 1) + combin(n - 1, r)

def combin(n, r):    
    assert n >= r
    return factorial(n) // (factorial(r) * factorial(n - r))

def permut(n, r):
    assert n >= r
    return factorial(n) // factorial(n - r)
