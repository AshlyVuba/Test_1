import pytest
import Solve

# Question 1: Even Sum Accumulator
# ===============================
def test_even_sum_negative_number():
    assert Solve.even_sum(-7) == 0

def test_even_sum_non_digit():
    with pytest.raises(TypeError):
        Solve.even_sum("banana")

def test_even_sum_no_input():
    with pytest.raises(TypeError):
        Solve.even_sum()

def test_even_sum_zero_input():
    assert Solve.even_sum(0) == 0

def test_even_sum_odd_input():
    assert Solve.even_sum(7) == 12

def test_even_sum_even_input():
    assert Solve.even_sum(6) == 12


# Question 2: Temperature Converter
# ===============================
def test_fahre_to_cels_negative():
    assert Solve.fahre_to_cels(-7) == -21.67

def test_fahre_to_cels_non_digit():
    with pytest.raises(TypeError):
        Solve.fahre_to_cels("blue")

def test_fahre_to_cels_no_input():
    with pytest.raises(TypeError):
        Solve.fahre_to_cels()

def test_fahre_to_cels_zero():
    assert Solve.fahre_to_cels(0) == -17.78

def test_fahre_to_cels_negative_crossover():
    assert Solve.fahre_to_cels(-40) == -40.00

def test_fahre_to_cels_boundary():
    assert Solve.fahre_to_cels(98.6) == 37.00


# Question 3: Palindrome Detector
# ===============================
def test_is_palindrome_non_str():
    with pytest.raises(TypeError):
        Solve.is_palindrome(154)

def test_is_palindrome_capitalized():
    assert Solve.is_palindrome("Bob") is True

def test_is_palindrome_mixed_capitalization():
    assert Solve.is_palindrome("kAyAk") is True

def test_is_palindrome_space():
    assert Solve.is_palindrome(" LEvel  ") is True

def test_is_palindrome_phrase():
    assert Solve.is_palindrome("Nurses run") is True

def test_is_palindrome_sentence():
    assert Solve.is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false_case():
    assert Solve.is_palindrome("Python") is False


# Question 4: Repeater Script
# ===============================
def test_repeat_script_simple():
    assert Solve.repeat_script("pops", 4) == "popspopspopspops"

def test_repeat_script_no_input():
    with pytest.raises(TypeError):
        Solve.repeat_script()

def test_repeat_script_incorrect_type():
    with pytest.raises(TypeError):
        Solve.repeat_script("Pop", "K")

def test_repeat_script_negative():
    with pytest.raises(ValueError):
        Solve.repeat_script("Pop", -7)


# Question 5: Cheapest Item Finder
# ===============================
def test_find_cheapest_standard():
    inventory = {"Laptop": 1200.00, "Mouse": 25.50, "Keyboard": 45.00}
    assert Solve.find_the_cheapest(inventory) == "Mouse"

def test_find_cheapest_unordered():
    inventory = {"Desk": 150.0, "Lamp": 15.99, "Pencil": 0.55}
    assert Solve.find_the_cheapest(inventory) == "Pencil"

def test_find_cheapest_tie():
    inventory = {"Apple": 0.99, "Pear": 0.99}
    assert Solve.find_the_cheapest(inventory) == "Apple"

def test_find_cheapest_empty():
    assert Solve.find_the_cheapest({}) is None


# Question 6: Email Sanitizer
# ===============================
def test_email_refiner_duplicates():
    emails = ["tester@example.com", "TESTER@EXAMPLE.COM", "  tester@example.com"]
    assert sorted(Solve.email_refiner(emails)) == ["tester@example.com"]

def test_email_refiner_messy():
    messy = ["  admin@site.org", "SUPPORT@help.net  ", "\tinfo@data.io\n"]
    expected = ["admin@site.org", "info@data.io", "support@help.net"]
    assert sorted(Solve.email_refiner(messy)) == sorted(expected)


# Question 7: Receipt Aligner
# ===============================
def test_receipt_formatter_standard():
    item, price = "Blinds", 10.20
    price_tag = f"R{price:.2f}"
    expected = f"{item:<10}{price_tag:>15}"
    assert Solve.receipt_formatter(item, price) == expected

def test_receipt_formatter_long_name():
    item, price = "Extra Large Pepperoni Pizza", 99.99
    result = Solve.receipt_formatter(item, price)
    assert len(result) == 25

def test_receipt_formatter_rounding():
    item, price = "Apple", 0.559
    price_tag = "R0.56"
    expected = f"{item:<10}{price_tag:>15}"
    assert Solve.receipt_formatter(item, price) == expected

def test_receipt_formatter_negative():
    with pytest.raises(ValueError):
        Solve.receipt_formatter("Discount", -5.00)