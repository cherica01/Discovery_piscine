import sys
 
p = sys.argv[1:]
print('parameters:',len(p))
for u in p :
 print(f'{u}: {len(u)}' )
