import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeuds[1] = (1, 0)

        # Définir une entrée correcte
        r.definir_entree(0)
        self.assertEqual(r.noeud_entree, 0)

        # Définir une entrée inexistante
        r.definir_entree(99)
        self.assertEqual(r.noeud_entree, -1)

    def test_ajout_noeud(self):
        r = Reseau()

        # Ajouter un nœud
        r.ajouter_noeud(0, (0, 0))
        self.assertIn(0, r.noeuds)
        self.assertEqual(r.noeuds[0], (0, 0))

        # Ajouter un autre nœud
        r.ajouter_noeud(1, (1, 1))
        self.assertIn(1, r.noeuds)
        self.assertEqual(r.noeuds[1], (1, 1))

    def test_ajout_arc(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeuds[1] = (1, 0)

        # Ajouter un arc valide
        r.ajouter_arc(0, 1)
        self.assertIn((0, 1), r.arcs)

        # Ajouter un arc qui existe déjà
        r.ajouter_arc(0, 1)
        self.assertEqual(len(r.arcs), 1)  # Pas de duplication d'arcs

        # Ajouter un arc entre des nœuds inexistants
        r.ajouter_arc(0, 99)
        self.assertNotIn((0, 99), r.arcs)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))