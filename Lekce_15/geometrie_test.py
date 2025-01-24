# geometrie_test.py

import unittest
import geometrie as g

# obvod, obsah kruhu
# trujúhelníková nerovnost
# objem cilindru

class TesGeometrie(unittest.TestCase):
    def test_get_triangle_perimeter(self):
        result = g.get_triangle_perimeter(10, 10, 10)
        self.assertEqual(result, 30)

    def test_triangle_validity_10_10_10(self):
        result = g.is_valid_triangle(10, 10, 10)
        self.assertTrue(result)

    def test_triangle_validity_10_10_100(self):
        result = g.is_valid_triangle(10, 10, 100)
        self.assertFalse(result)

    def test_triangle_validity_10_10_n10(self):
        result = g.is_valid_triangle(10, 10, -10)
        self.assertFalse(result)

    def test_get_square_area_10(self):
        result = g.get_square_area(10)
        self.assertEqual(result, 100)
    
    def test_get_square_area_100(self):
        result = g.get_square_area(100)
        self.assertEqual(result, 10000)

    def test_get_square_area_n10(self):
        with self.assertRaises(ValueError):
            g.get_square_area(-10)

    def test_get_circle_perimeter(self):
        pass

    def test_get_circle_content(self):
        pass
    
    def test_cone_volume(self):
        pass



unittest.main()

