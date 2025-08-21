import sys
import re
 
p = sys.argv[1:]
if len(p)!= 1 :
 print('none ')
else :
 m=p[0]
 t=input("What was the parameter?:")
 if m==t :
  print("Godd job")
 else :
  print('nope,sorry')
