#!/usr/bin/env python3
# coding: utf-8

"""
This problem was asked by Twitter. [MEDIUM] 8-17-20

Given a string with lowercase characters and left and right parentheses, remove the minimum number of parentheses so that the string is valid.

For example, if the string is ")a(b((cd)e(f)g)" then return "ab((cd)e(f)g)".
"""


def bracket_corrector(s):
    #First: set up counters & values, we are going to make two passes, once forward then backwards
    length = len(s)
    forward_counter = 0
    reverse_counter = 0
    values = {'(': 1, ')': -1}

    bad_indices = []

    #Second: make the forward pass, this finds the indices where there are excess closing parentheses
    for i,char in enumerate(s):
        #print('i Index: %i, Character: %s' % (i, char))
        if char in values:
            forward_counter += values[char]
            if values[char] < 0 and forward_counter < 0:
                bad_indices.append(i)

    #print('Bad index list after forward pass')
    #print(bad_indices)

    #Third: make the backwards pass, this finds the indices where there are excess opening parentheses
    for j,char in enumerate(s[::-1]):
        #print('j Index: %i, Character: %s' % (j, char))
        if char in values:
            reverse_counter += values[char]
            if values[char] > 0 and reverse_counter > 0:
                flipped_index = length - j - 1
                #print('Flipped Index: %i' % flipped_index)
                bad_indices.append(flipped_index)

    #print('Final list of bad indices')
    #print(bad_indices)

    #Fourth: construct new string, excluding the bad indices
    newstring = ''
    for k,char in enumerate(s):
        if k in bad_indices:
            continue
        newstring += char

    return newstring

    #This code makes 3 passes over the initial string, doing potentially O(1) operations at each point, therefore
    #it runs in O(n) time.  The number of bad indices is potentially O(n), therefore it requires O(n) extra space as well.

if __name__=='__main__':
    string = str(input())
    print(bracket_corrector(string))
