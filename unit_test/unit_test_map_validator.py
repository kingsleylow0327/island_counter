import sys
sys.path.append("../")
import unittest  # noqa E402
from helper.map_validator import map_validate  # noqa E402


class MapValidatorTest(unittest.TestCase):
    def test_map_validator_ok(self):
        array1 = ["00", "00"]
        val1 = map_validate(array1)
        self.assertEqual(val1["status"], "Ok")
        self.assertEqual(val1["message"], [['0', '0'], ['0', '0']])

        array2 = ["10", "00 "]
        val2 = map_validate(array2)
        self.assertEqual(val2["status"], "Ok")
        self.assertEqual(val2["message"], [['1', '0'], ['0', '0']])

    def test_map_validator_wrong_size(self):
        array1 = ["00", "1"]
        val1 = map_validate(array1)
        self.assertEqual(val1["status"], "Error")
        self.assertEqual(val1["message"], "Map shape of is not x*y")

        array2 = ["1", "10"]
        val2 = map_validate(array2)
        self.assertEqual(val2["status"], "Error")
        self.assertEqual(val2["message"], "Map shape of is not x*y")

    def test_map_validator_empty_lines(self):
        array1 = ["00", "", "01"]
        val1 = map_validate(array1)
        self.assertEqual(val1["status"], "Error")
        self.assertEqual(val1["message"], "Map contained exessive empty lines")

        array2 = ["00", "01", ""]
        val2 = map_validate(array2)
        self.assertEqual(val2["status"], "Error")
        self.assertEqual(val2["message"], "Map contained exessive empty lines")

    def test_map_validator_wrong_charactor(self):
        array1 = ["100", "0ab", "111"]
        val1 = map_validate(array1)
        self.assertEqual(val1["status"], "Error")
        self.assertEqual(val1["message"], "Map contained characters other than '0' & '1'")  # noqa E501

        array2 = ["100", "1 0", "111"]
        val2 = map_validate(array2)
        self.assertEqual(val2["status"], "Error")
        self.assertEqual(val2["message"], "Map contained characters other than '0' & '1'")  # noqa E501


if __name__ == "__main__":
    unittest.main()
