# Password Generator 🔐

This is a simple Python program that generates random passwords and also tells whether the password is strong or not. I made this project to practice Python basics like functions, loops and strings.

---

## Features

* Generate passwords of any length
* Can generate multiple passwords at once
* Option to include symbols
* Checks password strength (Weak / Moderate / Strong)

---

## How to Run

1. Make sure Python is installed
2. Open terminal in the folder
3. Run:

python pass.py


4. Enter the required inputs

---

## Example


Enter password length: 8
How many passwords: 2
Include symbols? (y/n): y

1. Ab3@kLp2  ->  Strong
2. mN7#xY9!  ->  Strong


---

## How it works

* It uses the `string` module to get letters and digits
* Based on user input, symbols are added
* Random characters are selected using `random.choice()`
* A loop is used to build the password
* Strength is checked mainly using length and mix of characters

---

## Author

Chhavi Soni
NIMS University

---

## Note

This is a basic project made for practice. I will try to improve it later by adding more options and better logic.
