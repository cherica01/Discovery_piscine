#!/usr/bin/env python3
def find_the_redheads(personnes) :
 def est_rousse(item):
  prenom, couleur = item 
  return couleur.lower() in ['roux','rousse']
 prenom_filt = filter(est_rousse,personnes.items())
 list_rousse = list(prenom for prenom ,_ in prenom_filt)
 return list_rousse

def main():
 personne = {
  'rqkoto':'roux',
  'bekoto':'mahaleo',
  'charle':'rousse'
}
 resultat = find_the_redheads(personne)
 print(resultat)

 

if __name__== '__main__':
 main()
