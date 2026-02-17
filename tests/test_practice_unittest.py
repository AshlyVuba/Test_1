import unittest
import Solve


#Question 1
class TestEvenSum(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(Solve.even_sum(-7),0)
    def test_non_digit(self):
        self.assertRaises(TypeError,Solve.even_sum,"banana")
    def test_no_input(self):
        self.assertRaises(TypeError,Solve.even_sum)
    def test_zero_input(self):
        self.assertEqual(Solve.even_sum(0),0)
    def test_odd_input(self):
        self.assertEqual(Solve.even_sum(7),12)
    def test_even_input(self):
        self.assertEqual(Solve.even_sum(6),12)

#_____________________________________________________________________________________________________________________
#Question 2
class TestFahreToCels(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(Solve.fahre_to_cels(-7),-21.67)
    def test_non_digit(self):
        self.assertRaises(TypeError,Solve.fahre_to_cels,"blue")
    def test_no_input(self):
        self.assertRaises(TypeError,Solve.fahre_to_cels)
    def test_zero_input(self):
        self.assertEqual(Solve.fahre_to_cels(0),-17.78)
    def test_zero_input(self):
        self.assertEqual(Solve.fahre_to_cels(-40),-40.00)
    def test_boundary(self):
        self.assertEqual(Solve.fahre_to_cels(98.6),37.00)

#_____________________________________________________________________________________________________________________
#Question 3

class TestIsPalindrome(unittest.TestCase):
    def test_non_str(self):
        self.assertRaises(TypeError,Solve.is_palindrome,154)
    def test_capitalized(self):
        self.assertEqual(Solve.is_palindrome("Bob"),True)
    def test_mixed_capitalization(self):
        self.assertTrue(Solve.is_palindrome("kAyAk"))
    def test_space(self):
        self.assertTrue(Solve.is_palindrome(" LEvel  "))
    def test_phrase(self):
        self.assertTrue(Solve.is_palindrome("Nurses run"))
    def test_sentence(self):
        self.assertTrue(Solve.is_palindrome("A man a plan a canal Panama"))
    def test_not_palindrome(self):
        self.assertFalse(Solve.is_palindrome("Python"))

#_____________________________________________________________________________________________________________________
#Question 4

class TestRepeatScript(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(Solve.repeat_script("pops",7))
    