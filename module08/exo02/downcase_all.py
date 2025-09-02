#!/usr/bin/env python3
import  sys
def downcqse_it(l):
 return l.lower()

if len(sys.argv) == 1:
 print('none')
else:
 for arg in sys.argv[1:]:
  print(downcqse_it(arg))
