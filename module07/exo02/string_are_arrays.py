import sys
import re
 
p = sys.argv[1:]
if len(p)!= 1 :
 print('none ')
else :
 m=p[0]
 t=m.count('z')

 if t>0 :
  print("z"*t)
 else :
  print('none')
