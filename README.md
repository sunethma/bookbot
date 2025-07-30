# 📚  bookbot - - Word & Character Frequency Counter

BookBot is my first [Boot.dev](https://www.boot.dev) project!

Welcome to **BookBot**, a Python-based command-line utility that reads a book (or any text file) and provides:

- 📖 **Total word count**
- 🔠 **Character frequency count** (including spaces and punctuation)
- 🔤 **Sorted character counts** (optional extension possible)

---

## 🧾 How It Works

The program takes the path to a `.txt` file as a command-line argument, processes the content, and returns:

- The **number of words** in the text
- A dictionary showing **each character** (case-insensitive) and how many times it appears

---

## 🗂 Project Structure

BOOKBOT/
├── __pycache__/
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py
├── stats.py
└── README.md

---

## 🚀 How to Run

### ✅ Prerequisites

- Python 3.6+

### ✅ Run the Program

```bash
python3 main.py books/frankenstein.txt

Or with your own .txt file:
python3 main.py path/to/your/book.txt

⚠️ Usage Notes
Make sure you run the script with one argument only: the path to the book file.

If no file path or an incorrect path is provided, the program will exit with a helpful message.

🔍 Sample Output

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============


## ✨ Features
✅ Case-insensitive character counting

✅ Includes all characters (spaces, punctuation, digits)

✅ Clean dictionary output for further analysis


## 🧑‍💻 Author
Created by Sunethma Welathanthri


