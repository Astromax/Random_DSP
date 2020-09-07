#!/usr/bin/env python3
# coding: utf-8

def longest_palindromic_subset(X):
    x = str(X)
    n = len(x)
    l = [1] * n
    for j in range(1, n):
        l_j = l[j] #current value of l[j]
        for i in reversed(range(j)):
            l_i = l[i] #current value of l[i]
            if x[i] == x[j]:
                l[i] = 2 + l_j if i < j-1 else 2 #check for i < j-1
            else:
                l[i] = max(l[i + 1], l[i])
                l_j = l_i
    return l[0]

if __name__=='__main__':
    X = int(input())
    print(longest_palindromic_subset(X))
