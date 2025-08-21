import sys
import re
 
p = sys.argv[1:]
if len(p)!= 2 :
 print('none ')
else :
 m=p[0]
 t=p[1]
 occ=re.findall(re.escape(m),t)
 if len(occ)==0 :
  print("none")
 else :
  print(len(occ))

