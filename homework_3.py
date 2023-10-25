""" Chapter #5 - Discussion Problem #1(c,e,g) (pg. 169/170) """
print("*** CHAPTER 5 - Problem 1 ***")
s1 = "spam"
s2 = "ni!"
# c
print(s1[1])
# e
print(s1[2] + s2[:2])
# g
print(s1.upper())

""" Chapter #5 - Discussion Problem #2(a,d,e) (pg. 170) """
print("*** CHAPTER 5 - Problem 2 ***")
# a
print(s2.upper())
# d
print(s1)
# e
print([s1[:2], s1[3]])

""" Chapter #5 - Discussion Problem #3(b,c,e) (pg. 170) """
print("*** CHAPTER 5 - Problem 3 ***")
# b
for w in "Now is the winter of our discontent ... ". split():
    print(w)
# c
for w in "Mississippi ". split(" i"):
    print(w, end=" ")
# e
msg = ""
for ch in " secret ":
    msg = msg + chr(ord(ch) + 1)
    print(msg)

# 4
print("*** Problem 4 ***")
grades_1 = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAA"
f = 0
d = 0
c = 0
b = 0
a = 0
for i in grades_1:
    if i == "F":
        f += 1
    elif i == "D":
        d += 1
    elif i == "C":
        c += 1
    elif i == "B":
        b += 1
    elif i == "A":
        a += 1

print('grades = "', end='')

for _ in range(f):
    print('F', end='')

for _ in range(d):
    print('D', end='')

for _ in range(c):
    print('C', end='')

for _ in range(b):
    print('B', end='')

for _ in range(a):
    print('A', end='')

print('"')

""" Chapter #5 - Programming Exercise #3 (pg. 171) """

score = int(input("Enter your exam score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

""" Chapter #5 - Programming Exercise #4 (pg. 171) """
print("*** CHAPTER 5 - Problem 4 ***")

phrase = input("Enter a phrase: ")
words = phrase.split()
acronym = ""
for word in words:
    acronym += word[0].upper()
print("Your acronym is:", acronym)

""" Chapter #5 - Programming Exercise #5 (pg. 171/172) """
print("*** CHAPTER 5 - Problem 5 ***")

def numeric_value(name):
    name = name.lower()
    value = 0
    for letter in name:
        if letter.isalpha():
            value += ord(letter) - ord('a') + 1
    return value

name = input("Enter a name: ")
value = numeric_value(name)
print("Numeric value:", value)