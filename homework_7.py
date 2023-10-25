""" Discussion Question 1 (pg. 278) """
"""
a) Definite loop vs. Indefinite loop
Definite loop ---> 	It is a loop that iterates a specific number of times which means it is controlled 
by a counter or a sequence.	Example for i in range(10): ...

Indefinite loop ---> A loop that iterates until a specific condition is met. It is controlled by a Boolean condition.
Example a "while condition:"

b) For loop vs. While loop
For loop ---> Iterates over a sequence or a range of values. It is used when the number of iterations is known beforehand.

While loop ---> Iterates until a condition is met. 	Used when the number of iterations is unknown or depends on a condition.

c) Interactive loop vs. Sentinel loop
Interactive loop ---> Continuously prompts the user for input and processes it. It is terminated 
by user input or an explicit break statement. Example a calculator program that prompts for operands and operations.

Sentinel loop ---> Iterates until a specific sentinel value is encountered. It is terminated 
when the sentinel value is encountered. Reading input values until a specific value (e.g., -1) is entered.

d) Sentinel loop vs. End-of-file loop

Sentinel loop ---> Terminated when a specific sentinel value is encountered. It is used 
when the input stream may contain multiple sets of data. Example, reading input values until a 
specific value (e.g., -1) is entered.

End-of-file loop ---> Terminated when the end of the input file is reached. Used when processing an entire input file. 
Example, processing lines of a text file until the end of the file is reached. 

"""

""" Discussion Question 2 (all sub-problems) (pg. 278/279) """
# You will find the truth table called "homework_7_truthtable" attached in this respository

""" Discussion Question 3 (a,c) (pg. 279) """
#a
n = int(input("Enter a positive integer: "))
sum_n = 0
count = 1
while count <= n:
    sum_n += count
    count += 1
print("Sum of the first", n, "counting numbers is:", sum_n)

#b
sum_series = 0
while True:
    num = int(input("Enter a number (enter 999 to stop): "))
    if num == 999:
        break
    sum_series += num
print("Sum of the series is:", sum_series)

""" Programming Exercise 1 (pg. 279) """
def syracuse_sequence(n):
    while n != 1:
        print(n, end=' -> ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

start_number = int(input("Enter a starting natural number: "))
syracuse_sequence(start_number)
