import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        t = Terrain()
        t.charger("terrains/t1.txt")  # Assurez-vous que t1.txt est correct

        # Vérifiez les dimensions
        self.assertEqual(t.largeur, 20)  # Modifier selon votre fichier
        self.assertEqual(t.hauteur, 10)  # Modifier selon votre fichier

        # Vérifiez quelques cases
        self.assertEqual(t.cases[0][0], Case.VIDE)
        self.assertEqual(t.cases[1][0], Case.CLIENT)
        self.assertEqual(t.cases[9][19], Case.ENTREE)  # Modifier en fonction de t1.txt

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))
