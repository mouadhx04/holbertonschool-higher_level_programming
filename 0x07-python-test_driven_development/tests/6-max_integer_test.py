#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_variable(self):
        a = 77
        self.assertEqual(max_integer([a]), a)

    def test_multiple_variables(self):
        a = 99
        self.assertEqual(max_integer([a, a, a]), a)

    def test_floats(self):
        self.assertEqual(max_integer([4, 4.4, 4.8]), 4.8)

    def test_regular_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_ints(self):
        self.assertEqual(max_integer([2, 1, 4, 3]), 4)

    def test_astring(self):
        self.assertEqual(max_integer("a crazy string here!"), 'z')

    def test_listoftuples(self):
        self.assertEqual(max_integer([(1, 1), (99, 99)]), (99, 99))

    def test_atuples(self):
        self.assertEqual(max_integer((1, 99, 5, 8)), 99)

    def test_large_intbeg(self):
        self.assertEqual(max_integer([999999999999999, 1]), 999999999999999)

    def test_large_smallbeg(self):
        self.assertEqual(max_integer([1, 999999999999999]), 999999999999999)

    def test_boolean(self):
        self.assertEqual(max_integer([True, False, 1, 2, 3]), 3)

    def test_negatives(self):
        self.assertEqual(max_integer([-5, -1, -8]), -1)

    def test_emptylist(self):
        self.assertIsNone(max_integer([]))

    def test_noargs(self):
        self.assertIsNone(max_integer())

    def test_none_in_list(self):
        self.assertIsNone(max_integer([None]))


class ExpectedFailureTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_listofsets(self):
        self.assertEqual(max_integer([{5, 7}, {5, 1, 99}]), {5, 7, 99})

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer(["hi", 1, 2, 3])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_none1(self):
        with self.assertRaises(TypeError):
            max_integer([None, 5])

    def test_none2(self):
        with self.assertRaises(TypeError):
            max_integer([4, None, 5])

    def test_none3(self):
        with self.assertRaises(TypeError):
            max_integer([4, None])

    def test_none4(self):
        with self.assertRaises(TypeError):
            max_integer([None, None, None])

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], [4, 5])

    def test_set(self):
        with self.assertRaises(TypeError):
            max_integer({5, 8, 0, 99})

if __name__ == '__main__':
    unittest.main()
