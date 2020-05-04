# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:55:01 2020

@author: Akash rana
"""
# Nested list problem of hacker rank
n = []
s = []
if __name__ =="__main__":
    for i in range(int(input())):
        name = str(input(""))
        score = float(input())
        n = n + [[name,score]]
        s = s + [score]
    new = sorted((set(s)))[1]
    for nam,scor in sorted(n):
        if(scor == new):
            print(nam)