#!/usr/bin/env python3
def creer_nom_comp(dict) :
 noms_comp = []
 for nom , prenom in dict.items() :
  nom_cap = nom.capitalize()
  prenom_cap = prenom.capitalize()
  noms_comp.append(f'{nom_cap} {prenom_cap}')
 return noms_comp
def main():
 personne = {
  'rqkoto':'fra',
  'bekoto':'mahaleo',
  'charle':'richard'
}
 resultat = creer_nom_comp(personne)
 print(resultat)

 

if __name__== '__main__':
 main()
