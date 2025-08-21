import sys 
p = sys.argv[1:]
if p :
 m=[p.lower() for p in p ]
 print(' '.join(m))
else :
 print('erreur')
