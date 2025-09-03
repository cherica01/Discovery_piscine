import sys
import re
 
p = sys.argv[1:]
if len(p)!= 2 :
 print('none ')
else :
 a=int(p[0])
 b=int(p[1])

 if b>a :
  t = list(range(a,b+1))
  print(t)
 else :
  print('none')
