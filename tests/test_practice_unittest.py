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
    def test_negative_crossover(self):
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
    def test_simple_input(self):
        self.assertEqual(Solve.repeat_script("pops",4),"popspopspopspops")
    def test_no_input(self):
        self.assertRaises(TypeError,Solve.repeat_script)
    def test_incorrect_input_type(self):
        self.assertRaises(TypeError,Solve.repeat_script,"Pop","K")
    def test_negative_number(self):
        self.assertRaises(ValueError,Solve.repeat_script,"Pop",-7)
    def test_missing_input(self):
        self.assertRaises(TypeError,Solve.repeat_script,"Wrong")

#_____________________________________________________________________________________________________________________
#Question 5

class TestFindTheCheapest(unittest.TestCase):
    def test_correct_item(self):
        # Clearly defined prices, added in a specific order
        inventory_1 = {
            "Laptop": 1200.00,
            "Mouse": 25.50,
            "Keyboard": 45.00,
            "Monitor": 300.00
        }
        # Expected Result: "Mouse"
        self.assertEqual(Solve.find_the_cheapest(inventory_1),"Mouse")

    def test_unordered_list(self):
        # Cheapest item is buried in the middle with many decimals
        inventory_2 = {
            "Desk": 150.00,
            "Lamp": 15.99,
            "Pencil": 0.55,
            "Chair": 85.00,
            "Notebook": 2.49
        }
        # Expected Result: "Pencil"
        self.assertEqual(Solve.find_the_cheapest(inventory_2),"Pencil")

    def test_same_price(self):
        # Two items share the same lowest price
        inventory_3 = {
            "Apple": 0.99,
            "Banana": 1.50,
            "Pear": 0.99,
            "Orange": 2.00
        }
        # Expected Result: "Apple" (if returning the first one found)
        self.assertEqual(Solve.find_the_cheapest(inventory_3),"Apple")
    
    def test_discount_item(self):
        # Testing zeros and negatives
        inventory_4 = {
            "Service_Fee": 10.00,
            "Promotion": -5.00,
            "Water": 0.00,
            "Bread": 2.50
        }
        # Expected Result: "Promotion"
        self.assertEqual(Solve.find_the_cheapest(inventory_4),"Promotion")

    def test_empty(self):
        inventory_5={}
        self.assertEqual(Solve.find_the_cheapest(inventory_5),None)

    def test_invalid_input(self):
        inventory_6=[3,"^","poop","lopo",7,9]
        self.assertRaises(TypeError,Solve.find_the_cheapest,inventory_6)

#_____________________________________________________________________________________________________________________
#Question 6

class TestEmailRefiner(unittest.TestCase):
    def test_correct_email(self):
        duplicates_list = [
        "tester@example.com",
        "TESTER@EXAMPLE.COM",
        "Tester@Example.com",
        "  tester@example.com",
        "tester@example.com  ",
        "  TeStEr@ExAmPlE.cOm  "
        ]
        self.assertEqual(sorted(Solve.email_refiner(duplicates_list)),["tester@example.com"])

    def test_messy_formating(self):
        messy_format_list = [
            "  admin@site.org", 
            "SUPPORT@help.net  ", 
            "\tinfo@data.io\n", 
            "  CONTACT@STUFF.biz  "
        ]
        # Expected Result: ["admin@site.org", "contact@stuff.biz", "info@data.io", "support@help.net"]
        self.assertEqual(sorted(Solve.email_refiner(messy_format_list)),["admin@site.org", "contact@stuff.biz", "info@data.io", "support@help.net"])

    def test_mixed_formatting(self):
        ultimate_list = [
            "bob@work.com",
            "  bob@work.com",
            "ALICE@home.com",
            "alice@home.com  ",
            "BOB@WORK.COM",
            "charles@school.edu",
            "  ALICE@HOME.COM  "
        ]
        # Expected Result (Sorted): ["alice@home.com", "bob@work.com", "charles@school.edu"]
        self.assertEqual(sorted(Solve.email_refiner(ultimate_list)),["alice@home.com", "bob@work.com", "charles@school.edu"])

    def test_invalid_input(self):
        self.assertRaises(TypeError, Solve.email_refiner, ["valid@test.com", 12345])

#_____________________________________________________________________________________________________________________
#Question 7

class TestReceiptFormater(unittest.TestCase):
    def test_correct_format(self):
        item="Blinds"
        price=10.20
        price_adjusted=f'{price:.2f}'
        self.assertEqual(Solve.receipt_formater("Blinds",10.20),f"{item:<10}{'R'+price_adjusted:>15}")

    def test_wrong_input(self):
        item="Popsicle"
        price="Ice"
        self.assertRaises(TypeError,Solve.receipt_formater,item,price)
    
    def test_no_item(self):
        item=None
        price=20.00
        self.assertRaises(TypeError,Solve.receipt_formater,item,price)