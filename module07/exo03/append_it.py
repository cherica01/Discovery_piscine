import sys
import re
 
p = sys.argv[1:]
if not p :
 print('print')
else :
 for u in p :
  pos = u.find('isme')
  if not (pos !=-1 and pos == len(u)-len('isme')):
   print(u + 'isme')
