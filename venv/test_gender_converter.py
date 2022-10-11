import unittest
from unittest import TestCase

class Test(TestCase):
    def test_convert_gender_when_male(self):
      actual = convert_gender("M")
      expected = "Male"
      self.assertEqual(actual, expected)

    def test_convert_gender_when_female(self):
      actual = convert_gender("F")
      expected = "Female"
      self.assertEqual(actual, expected)

    def test_convert_gender_when_unknown(self):
      actual = gender_converter("No Gender")
      expected = "Unknown_gender"
      self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
#    unittest.Test()
    #    unittest.main()