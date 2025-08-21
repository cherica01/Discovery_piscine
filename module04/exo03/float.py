i = input('GIve me a number :')
try :
 n = float(i)
 if n.is_integer() :
  print('This number isan integer')
 else:
  print('This number is a decimal') 
except ValueError :
 print('number invalide')
