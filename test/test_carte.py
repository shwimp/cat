import sys
sys.path.append("..")
import unittest

from src.carte import Carte

class TestCarte(unittest.TestCase):
    def test_get_adv_info(self):
        map_list = [['C', '3', '3'], ['A', 'test', '1', '0', 'N', 'AA']]
        carte = Carte(map_list)
        self.assertEqual(carte.adventurers, {'test': {'x': 1 , 'y': 0, 'direction': 'N', 'move': 'AA', 'treasures': 0}})

    def test_draw_map(self):
        map_list = [['C', '3', '4'], ['M', '1', '1'], ['T', '2', '2', '5']]
        carte = Carte(map_list)
        result = [['.', '.', '.'], ['.', 'M', '.'], ['.', '.', 5], ['.', '.', '.']]
        self.assertEqual(carte.map_array, result)

    def test_check_position_exeption(self):
        map_list = [['C', '3', '3'], ['M', '1', '0'], ['A', 'test', '1', '0', 'N', 'AA']]
        with self.assertRaises(Exception):
            Carte(map_list)

    def test_execute_orders_exception(self):
        map_list = [['C', '3', '3'], ['A', 'test', '1', '0', 'N', 'AZ']]
        carte = Carte(map_list)
        with self.assertRaises(Exception):
            carte.execute_orders()

if __name__ == '__main__':
    unittest.main()