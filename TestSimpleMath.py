from SimpleMAth import SimpleMath
import unittest

class TestSimpleMath(unittest.TestCase):
    def test(self):
        to_test = SimpleMath
        self.assertEqual(to_test.addition(1,2),3)
        self.assertEqual(to_test.soustraction(4,2),2)

if __name__ == "__main__":
    unittest.main()