
from Terrain import Terrain
from Reseau import Reseau

from StrategieReseau import StrategieReseauManuelle

if __name__ == "__main__":
    reseau = Reseau()
    terrain = Terrain()

    print("======================================")
    print("1. Configurer Chemin 1")
    print("2. Configurer Chemin 2")
    choix = input("Choisissez une option (1 ou 2) : ").strip()

    if choix == "1":
        terrain.charger("terrains/t1.txt")
        print("Chemin 1 sélectionné.")
    elif choix == "2":
        terrain.charger("terrains/t2.txt")  
        print("Chemin 2 sélectionné.")
    else:
        print("Option invalide.")
        exit()

    print("Terrain charge :")
    terrain.afficher()

    print("======= Configuration Automatique=======")
    reseau.configurer(terrain)
    if reseau.valider_reseau() and reseau.valider_distribution(terrain):
        print("Configuration valide simple trouvée")
        print("Cout : {}M€".format(reseau.calculer_cout(terrain)))
        reseau.afficher_avec_terrain(terrain)
    
    else:
        print("Pas de configuration valide trouvée.")

    print("======= Configuration Manuelle======")
    reseau.set_strategie(StrategieReseauManuelle())
    reseau.configurer(terrain)
    if reseau.valider_reseau() and reseau.valider_distribution(terrain):
        print("Configuration valide optimale trouvée")
        print("Cout : {}M€".format(reseau.calculer_cout(terrain)))
        reseau.afficher_avec_terrain(terrain)
    else:
        print("Pas de configuration valide optimale trouvée.")
