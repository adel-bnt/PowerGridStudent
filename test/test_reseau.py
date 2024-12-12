import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeuds[1] = (1, 0)

       
        r.definir_entree(0)
        self.assertEqual(r.noeud_entree, 0)

      
        r.definir_entree(99)
        self.assertEqual(r.noeud_entree, -1)

    def test_ajout_noeud(self):
        r = Reseau()

       
        r.ajouter_noeud(0, (0, 0))
        self.assertIn(0, r.noeuds)
        self.assertEqual(r.noeuds[0], (0, 0))
        
       
        r.ajouter_noeud(1, (1, 1))
        self.assertIn(1, r.noeuds)
        self.assertEqual(r.noeuds[1], (1, 1))

    def test_ajout_arc(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeuds[1] = (1, 0)

        
        r.ajouter_arc(0, 1)
        self.assertIn((0, 1), r.arcs)

        r.ajouter_arc(0, 1)
        self.assertEqual(len(r.arcs), 1)  

        
        r.ajouter_arc(0, 99)
        self.assertNotIn((0, 99), r.arcs)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))