#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:52:01 2020

@author: saurabhadhikary
"""

import random
s="123"
def get_rand():
  new_s = ''.join(random.sample(s,len(s)))
  return new_s
visited_s = []
mins = set()
for i in range(pow(2,len(s))):
  s = get_rand()
  if s not in visited_s:
    visited_s.append(s)
    if int(s)%30==0:
      mins.add(int(s))
try:
    print(max(mins))
except ValueError:
    print(-1)