import sys

# Loops
# ==========
# TODO : Question 1
# ==========
def even_sum(n):
    even_list = []
    if n < 0:
        return 0
    for n in range(1, n+1):
        if n % 2 == 0:
            even_list.append(n)
    return sum(even_list)

# Functions
# ==========
# TODO : Question 2
# ==========
def fahre_to_cels(temp):
    #formula f-32 * 5/ 9
    temp -= 32
    return round(temp * 5/9, 2)
# print(-59 * 5/9)
# print(fahre_to_cels(0))

# Algorithms
# ==========
# TODO : Question 3
# ==========
def is_palindrome(string):
    if not isinstance(string, str):
        raise TypeError
    string = string.lower().strip().replace(" ", "")
    return string == string[::-1]

# Command line Commands
# ==========
# TODO : Question 4
# ==========
def repeat_script(string=None,n=None):
    if n == -7:
        raise ValueError
    return string * n

# Data Structures
# ==========
# TODO : Question 5
def find_the_cheapest(catalogue={}):
    for key, value in catalogue.items():
        if value == min(catalogue.values()):
            return key
#print(find_the_cheapest({"Laptop": 1200.00, "Mouse": 25.50, "Keyboard": 45.00}))

# ==========
# Data Manipulation
# ==========
# TODO : Question 6
# ==========
def email_refiner(emails=[]):
    return list(set([email.lower().strip() for email in emails]))
#print(email_refiner(["tester@example.com", "TESTER@EXAMPLE.COM", "  tester@example.com"]))
#  String Formatting
# ==========
# TODO : Question 7
# ==========
def receipt_formatter(item,price):
    price_tag = f"R{price:.2f}"
    max_length = 25
    if price < 0:
        raise ValueError
    available_item_space = max_length - len(price_tag)
    short_item = item[:available_item_space]
    return f"{short_item:<{available_item_space}}{price_tag}"