# 🐍 Python Fundamentals Practice Test

This repository contains a series of exercises designed to test core Python proficiency, including loops, data structures, and string manipulation.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3 installed. You will also need `pytest` for running the modern test suite:
`pip install pytest`

### Running the Tests
You can verify your solutions in `solve.py` using either the standard library or pytest:

* **Unittest:** `python3 -m unittest tests/test_practice_unittest.py`
* **Pytest:** `python3 -m pytest tests/test_practice_pytest.py`

---

## 💻 Coding Questions

### 1. The Even Sum Accumulator (Loops)
Create logic that calculates the sum of all even integers from 1 up to a specified limit. 
* **Edge Cases:** Returns `0` if the limit is zero or negative.


### 2. Temperature Converter (Functions)
Transform a Fahrenheit temperature into Celsius.
* **Requirement:** Output must be a float rounded to exactly **two decimal places**.


### 3. Palindrome Detector (Algorithms)
Check if a string reads the same forward and backward.
* **Requirement:** Ignore letter casing and disregard all spaces.


### 4. Repeater Script (CLI)
A terminal-based script that accepts text and a number $n$.
* **Requirement:** Output the text repeated $n$ times as a single continuous string.


### 5. Cheapest Item Finder (Data Structures)
Search through a dictionary of products and prices.
* **Requirement:** Return the name of the cheapest product. Handle empty collections.


### 6. Email Sanitizer (Data Manipulation)
Accept a list of raw email strings.
* **Requirement:** Remove whitespace, convert to lowercase, and remove duplicates.


### 7. Receipt Aligner (String Formatting)
Produce a receipt line exactly **25 characters wide**.
* **Requirement:** Item name on the left, Price (prefixed with "R" and 2 decimals) on the right.

---

## 📚 Theory Questions
Answer the questions found in  inside the `[text](Theory_questions.txt)` file.[text](Answers.txt) Focus on explaining the "why" behind the logic.