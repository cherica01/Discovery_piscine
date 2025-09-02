#!/usr/bin/env python3
def greetinngs(n='noble stranger'):
 if not isinstance(n, str):
  print('error , is not a name') 
 else :
  print('hello',n)

greetinngs()
greetinngs('cherica')
greetinngs(111)
