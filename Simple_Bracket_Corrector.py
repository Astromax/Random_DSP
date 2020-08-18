#!/usr/bin/env python3
# coding: utf-8

"""
This problem was asked by Twitter. [MEDIUM] 8-17-20

Given a string with lowercase characters and left and right parentheses, remove the minimum number of parentheses so that the string is valid.

For example, if the string is ")a(b((cd)e(f)g)" then return "ab((cd)e(f)g)".
"""


def bracket_corrector(s):
    #Balance: each closing bracket must match an existing opening bracket
    #Keep track of brackets on a stack, characters can go about their business
    
    stack = []
    newstring = ['']*len(s)
    
    for i,char in enumerate(s):
        if char == '(':
            stack.append(i) #Add index of left parenthesis to the stack
        elif char == ')':
            idx = stack.pop()        #Retrieve index of most recent left parenthesis
            newstring[idx] = s[idx]  #Add left parenthesis
            newstring[i] = char      #Add right parenthesis
        else:
            newstring[i] = char  #Add non-parenthesis character
    
    #Join new string together & return
    return ''.join(newstring)

if __name__=='__main__':
    string = str(input())
    print(bracket_corrector(string))
