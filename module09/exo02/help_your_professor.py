#!/usr/bin/env python3
def average(notes):
 if not notes :
  return 0 
 total = sum(notes.values())
 nb_el = len(notes)
 moyenne = total /nb_el
 
 return moyenne 
 
 
def main():
 classe_3b = {
  'rqkoto':12,
  'bekoto':1,
  'charle':8
}
 classe_3a = {
  'rqkoto':12,
  'solo':8,
  'charle':8
}
 resultat1 =average(classe_3b)
 resultat2 =average(classe_3a)
 print(f'la moyenne du classe_3b est:{resultat1}' )
 print(f'la moyenne du classe_3a est:{resultat2}' )

if __name__== '__main__':
 main()
