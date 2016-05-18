import unittest
import hom

class TestHom(unittest.TestCase):
    
    def test_2_dim_2_holes1(self):
        self.assertEqual(hom.betti(2,'1,2,3 2,4 3,4 5'),[0,1,1,0])

    def test_2_dim_2_holes2(self):
        self.assertEqual(hom.betti(2,'1,2,3 1,3,4 2,3,4 2,5 4,5 6'),[0,1,1,0])

    def test_2_dim_2_holes_different_order(self):
        self.assertEqual(hom.betti(2,'3,4 1,2,3 2,4 5'),[0,1,1,0])

    def test_2_dim_1_hole(self):
        self.assertEqual(hom.betti(2,'1,2,3 2,3,4 5'),[0,1,0,0])

    def test_2_dim_1_hole_long_name(self):
        self.assertEqual(hom.betti(2,'11,12,13 12,13,14 15'),[0,1,0,0])

    def test_2_dim_empty(self):
        self.assertEqual(hom.betti(2,''),[0,0,0,0])

    def test_2_dim_1_elm(self):
        self.assertEqual(hom.betti(2,'1'),[0,0,0,0])

    def test_3_dim_2_holes(self):
        self.assertEqual(hom.betti(3,'1,2,3 1,2,4 1,3,4 2,3,4 1,5 3,5'),[0,0,1,1,0])

if __name__ == '__main__':
    unittest.main()

