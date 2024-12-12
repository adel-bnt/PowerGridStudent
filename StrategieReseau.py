from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []


class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []
        
        entree_coords = t.get_entree()
        print(f"Entrée électrique  en {entree_coords}")
        
    
        noeud_entree = 0
        noeuds[noeud_entree] = entree_coords
        
        
        while True:
            print("\nTerrain actuel :")
            t.afficher()
            print("\nRéseau actuel :")
            for n, coords in noeuds.items():
                print(f"  Nœud {n} : {coords}")
            
            action = input("\nAction (noeud / arc / finir) : ").strip().lower()
            
            if action == "noeud":
                try:
                    x, y = map(int, input("Coordonnées du nouveau nœud (x y) : ").split())
                    identifiant = len(noeuds)
                    noeuds[identifiant] = (x, y)
                    print(f"Nœud {identifiant} ajouté à {(x, y)}.")
                except ValueError:
                    print("Entrée invalide. Essayez à nouveau.")
            
            elif action == "arc":
                try:
                    n1, n2 = map(int, input("Identifiants des nœuds à connecter (n1 n2) : ").split())
                    if n1 in noeuds and n2 in noeuds:
                        arcs.append((n1, n2))
                        print(f"Arc ajouté entre {n1} et {n2}.")
                    else:
                        print("Un des nœuds spécifiés n'existe pas.")
                except ValueError:
                    print("Entrée invalide. Essayez à nouveau.")
            
            elif action == "finir":
                break
            
            else:
                print("Commande non reconnue. Essayez : ajouter noeud / ajouter arc / finir.")
        
        return noeud_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []

        
        entree_coords = t.get_entree()
        noeud_entree = 0
        noeuds[noeud_entree] = entree_coords

        clients = t.get_clients()
        for i, client in enumerate(clients, start=1):
            noeuds[i] = client
            arcs.append((noeud_entree, i))  

        print(f"[DEBUG] Nœuds générés : {noeuds}")
        print(f"[DEBUG] Arcs générés : {arcs}")
        return noeud_entree, noeuds, arcs
