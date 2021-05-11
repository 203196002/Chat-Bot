#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:59:25 2020

@author: saurabhadhikary
"""
i = input()
visited_s = []
mins = set()
from itertools import permutations

# this will create all permutations of length 3 of [0,1,2]
l = list(permutations(i, len(i)))
for s in l:
  new_s = ''.join(s)
  if new_s not in visited_s:    
    visited_s.append(new_s)
    if int(new_s)%30==0:
      mins.add(int(new_s))
try:
    print(max(mins))
except ValueError:
    print('-1')

