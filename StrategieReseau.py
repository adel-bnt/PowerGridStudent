from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []
        entree = t.get_entree()

        noeud_id = 0
        while True:
            t.afficher()
            print("Configuration manuelle")
            choix = input("Ajouter un noeud (y/n)? ")
            if choix.lower() != 'y':
                break
            ligne = int(input("Ligne : "))
            colonne = int(input("Colonne : "))
            noeuds[noeud_id] = (ligne, colonne)
            if noeud_id > 0:
                liaison = int(input(f"Relier à quel noeud existant (0 à {noeud_id - 1})? "))
                arcs.append((liaison, noeud_id))
            noeud_id += 1

        return entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []
        entree = t.get_entree()

        print("Entrée électrique :", entree)
        if entree == (-1, -1):
            print("Aucune entrée électrique trouvée dans le terrain.")
            return -1, {}, []

        # Ajouter le noeud d'entrée
        noeud_id = 0
        noeuds[noeud_id] = entree
        print("Noeuds après ajout de l'entrée :", noeuds)

        # Relier chaque client
        clients = t.get_clients()
        print("Clients :", clients)

        for client in clients:
            noeud_id += 1
            noeuds[noeud_id] = client

            # Connecter au noeud d'entrée ou à un autre client (chemin direct)
            chemin = self.trouver_chemin(entree, client, t)
            print(f"Chemin trouvé pour {client} :", chemin)
            dernier_noeud = 0  # Commencer depuis l'entrée
            for coord in chemin[1:]:
                if coord not in noeuds.values():
                    noeud_id += 1
                    noeuds[noeud_id] = coord
                suivant_noeud = [n for n, c in noeuds.items() if c == coord][0]
                arcs.append((dernier_noeud, suivant_noeud))
                dernier_noeud = suivant_noeud

        print("Noeuds finaux :", noeuds)
        print("Arcs finaux :", arcs)
        return 0, noeuds, arcs


