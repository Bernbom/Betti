import unittest
import hom

class TestHom(unittest.TestCase):
    
    def test_2_dim_2_holes1(self):
        self.assertEqual(hom.betti(2,'123 24 34 5'),[0,1,1,0])

    def test_2_dim_2_holes2(self):
        self.assertEqual(hom.betti(2,'123 134 234 25 45 6'),[0,1,1,0])

    def test_2_dim_2_holes_wrong_order(self):
        self.assertEqual(hom.betti(2,'34 123 24 5'),[0,1,1,0])

    def test_2_dim_1_hole(self):
        self.assertEqual(hom.betti(2,'123 234 5'),[0,1,0,0])

    def test_2_dim_empty(self):
        self.assertEqual(hom.betti(2,''),[0,0,0,0]) # fejler: giver [1,0,0,0]

    def test_2_dim_1_elm(self):
        self.assertEqual(hom.betti(2,'1'),[0,0,0,0])

    def test_3_dim_2_holes(self):
        self.assertEqual(hom.betti(3,'123 124 134 234 15 35'),[0,0,1,1,0])

if __name__ == '__main__':
    unittest.main()

