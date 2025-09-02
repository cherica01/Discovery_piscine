#!/usr/bin/env python3
import sys
def shrink(le):
 print(le[:8])
def enlarge(le):
 print(le + 'z'*(8-len(le)))
if len(sys.argv)==1:
 print('aucun argument')
else:
 for arg in sys.argv[1:]:
  if len(arg) > 8 :
   shrink(arg)
  elif len(arg)== 8 :
   print(arg)
  else :
   enlarge(arg)
