import sys 
p = sys.argv[1:]
if p :
 m=[p.upper() for p in p ]
 print(' '.join(m))
else :
 print('erreur')
