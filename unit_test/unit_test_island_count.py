import unittest
from unittest.mock import Mock
import sys
sys.path.append("../")
import island_counter as ic


class IslandCountTest(unittest.TestCase):
    def test_island_count_ok(self):
        ic.walk = Mock(return_value=None)
        array1 = [['0', '0'], ['0', '0']]
        val1 = ic.island_count(array1)
        self.assertEqual(ic.walk.call_count, 0)
        self.assertEqual(val1["status"], "Ok")
        self.assertEqual(val1["message"], "0")

        ic.walk.reset_mock()
        array2 = [['1', '0'], ['0', '1']]
        val2 = ic.island_count(array2)
        self.assertEqual(ic.walk.call_count, 2)
        self.assertEqual(val2["status"], "Ok")
        self.assertEqual(val2["message"], "2")

        ic.walk.reset_mock()
        array3 = [['1', '1'], ['0', '1']]
        val3 = ic.island_count(array3)
        self.assertEqual(ic.walk.call_count, 3)
        self.assertEqual(val3["status"], "Ok")
        self.assertEqual(val3["message"], "3")

    def test_island_count_empty(self):
        array1 = []
        val1 = ic.island_count(array1)
        self.assertEqual(val1["status"], "Error")
        self.assertEqual(val1["message"], "Empty Map")


if __name__ == "__main__":
    unittest.main()
