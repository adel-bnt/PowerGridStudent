from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto


class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []
        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            n1, n2 = n2, n1
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat




    def valider_reseau(self) -> bool:
        if self.noeud_entree == -1 or not self.noeuds:
            print("[DEBUG] Aucun nœud ou nœud d'entrée invalide.")
            return False

        visited = set()
        stack = [self.noeud_entree]

        # Parcours en profondeur pour vérifier la connectivité
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                
                # Ajouter les voisins connectés
                for n1, n2 in self.arcs:
                    if n1 == current and n2 not in visited:
                        stack.append(n2)
                    elif n2 == current and n1 not in visited:
                        stack.append(n1)


        print(f"[DEBUG] Nœuds visités : {visited}")
        return len(visited) == len(self.noeuds)


    def valider_distribution(self, t: Terrain) -> bool:
        if self.noeud_entree == -1:
            print("[DEBUG] Nœud d'entrée invalide.")
            return False

        clients = t.get_clients()

        # Vérifier que chaque client est couvert
        for client in clients:
            if client not in self.noeuds.values():
                print(f"[DEBUG] Client non relié : {client}")
                return False

        print("[DEBUG] Tous les clients sont reliés.")
        return True


    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs = self.strat.configurer(t)

    def afficher(self) -> None:
        print("=== Réseau ===")
        print("Nœud d'entrée :", self.noeud_entree)
        print("Nœuds du réseau :")
        for n, coords in self.noeuds.items():
            print(f"  Nœud {n} : {coords}")
        print("\nArcs du réseau :")
        for n1, n2 in self.arcs:
            print(f"  {n1} -> {n2}")

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    elif c == Case.CLIENT:
                        print("C", end="")
                    elif c == Case.VIDE:
                        print("~", end="")
                    elif c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    elif c == Case.CLIENT:
                        print("C", end="")
                    elif c == Case.VIDE:
                        print("+", end="")
                    elif c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        
        for _ in self.arcs:
            cout += 1.5
        # Coût des nœuds
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2  # 2M€ pour un nœud sur un obstacle
            else:
                cout += 1  # 1M€ pour un nœud sur une case normale
        return cout
