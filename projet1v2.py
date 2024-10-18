# importation fichier Json salaire
#import du json en chemin absolu, alias "data" dans la suite du code"""


import json

with open("/home/flavigny/Documents/simplon/employes-data-6710b180e7d62991266985.json", "r") as f:
    data = json.load(f)
#print(data)
#version chemin relatif


#definition de la fonction salaire, permettant de  calculer le salaire mensuel de chaque salarié
# calcul de l’overtime, si temps travaillé superieur au temps du contrat, passage en heure supplementaire majoré
#le salaire est calculé sur le temps de travail contractuel

def salaire(employe):

    overtime = employe["weekly_hours_worked"] - employe["contract_hours"] 
   
    salarybase = employe["hourly_rate"] * employe["contract_hours"]

    if overtime > 0:
            SalaryBonus = overtime * employe["hourly_rate"] * 1.5
    else:
         SalaryBonus = 0
    salarytotalhebdo = salarybase + SalaryBonus
    return 4 * salarytotalhebdo



#code et appel de la fonction avec rendu sur terminal

for Entreprise, employes in data.items():
    print("")
    print(f"Entreprise: {Entreprise}")
    print("")
    #mise en forme
    liste_des_salaires = []
    #creation de la liste des salaires ou ils seront stockes afin d’etre comparé par la suite
    for employe in employes:
        name = employe["name"]
        fonction = employe["job"]
        salairemensuel = salaire(employe)
        liste_des_salaires.append(salairemensuel)
    #ajout du salaire calculé dans la liste

        print(f"{name:<10} | {fonction:<15} | salaire mensuel : {salairemensuel:.2f}€")
    print("")
    print("")
    print("=" * 60)
    print("")
#mise en forme

    salaire_moyen = sum(liste_des_salaires) / len(liste_des_salaires)
    salaire_max = max(liste_des_salaires)
    salaire_min = min(liste_des_salaires)
    print(f"Statistique des salaires pour l’entreprise {Entreprise}")
    print(f"Salaire moyen: {salaire_moyen:.2f}€")
    print(f"Salaire le plus élevé: {salaire_max:.2f}€")
    print(f"Salaire le plus faible: {salaire_min:.2f}€")
    print("")
    print("=" * 60)
#affichage des statistiques par entreprises avec mise en forme.

