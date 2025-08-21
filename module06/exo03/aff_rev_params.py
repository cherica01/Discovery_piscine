import sys 
p = sys.argv[1:]
if len(p)< 2 :
 print('none ')
else :
 for p in reversed(p):
  print(p)
