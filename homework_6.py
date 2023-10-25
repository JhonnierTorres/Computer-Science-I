""" Chapter #7 - Discusson Problem #2 (pg.237) """

"""
Similarities:
1. Both approaches involve identifying and addressing potential errors or exceptions within a program or algorithm.
2. They both allow for customized handling of specific situations, rather than simply relying on default or generic behaviors.
3. Both techniques can improve the overall reliability and stability of a program by proactively addressing potential issues before they become major problems.

Differences:

try-except:

- Purpose: Primarily used for handling unexpected errors that arise during program execution.
- Mechanism: Employs a specialized structure (try-except block) to capture and handle exceptions.
- Scope: Can handle a wide range of errors, including system-generated errors and custom exceptions.

if-else:

- Purpose: Primarily used for handling expected exceptional cases based on specific conditions.
- Mechanism: Utilizes conditional statements (if-else) to check for specific conditions and execute corresponding code.
- Scope: Limited to handling anticipated exceptional cases that can be explicitly checked for.
"""

""" Chapter #7 - Programming Exercise #3 (pg. 239) """

exam_score = int(input("Enter the exam score: "))

if exam_score >= 90:
    grade = "A"
elif exam_score >= 80:
    grade = "B"
elif exam_score >= 70:
    grade = "C"
elif exam_score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is: ", grade)

""" Chapter #7 - Programming Exercise #7 (pg. 239) """


def babysitting_bill(start_time, end_time):
    daytime_rate = 2.50
    nighttime_rate = 1.75

    start_minutes = start_time[0] * 60 + start_time[1]
    end_minutes = end_time[0] * 60 + end_time[1]

    total_bill = 0.0

    while start_minutes < end_minutes:
        if start_minutes < 9 * 60:
            # apply the daytime rate
            total_bill += min(9 * 60 - start_minutes, 60) / 60 * daytime_rate
        else:
            # apply the nighttime rate
            total_bill += min(24 * 60 - start_minutes, 60) / 60 * nighttime_rate

        start_minutes += 60
    return total_bill


start_hour = int(input("Enter the starting hour (24-hour format): "))
start_minute = int(input("Enter the starting minute: "))
end_hour = int(input("Enter the ending hour (24-hour format): "))
end_minute = int(input("Enter the ending minute: "))

start_time = (start_hour, start_minute)
end_time = (end_hour, end_minute)
total_bill = babysitting_bill(start_time, end_time)

print("Total babysitting bill: $%.2f" % total_bill)

""" Chapter #7 - Programming Exercise #8 (pg. 239) """
age = int(input("Enter the person's age: "))
years_of_citizenship = int(input("Enter the person's years of US citizenship: "))

# Senate
if age >= 30 and years_of_citizenship >= 9:
  senate_eligibility = "Eligible for Senate"
else:
  senate_eligibility = "Not eligible for Senate"

# House
if age >= 25 and years_of_citizenship >= 7:
  house_eligibility = "Eligible for House"
else:
  house_eligibility = "Not eligible for House"

print("Senate eligibility:", senate_eligibility)
print("House eligibility:", house_eligibility)

""" Modify a program from a previous homework assignment so that it utilizes exception handling to prevent at least two conceivable run-time errors. Explain what these errors are and how the program will respond """

""" Chapter #6 - Programming Exercise #12 

def sumList(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum

lista = ([10, 6, 20, 23])
test = sumList(lista)
print("The test result i: ", test) 
"""
def sumList(nums):
    total = 0
    for num in nums:
        total += num
    return total

try:
    lista = [10, 6, 20, 23]
    test = sumList(lista)
    print("The test result is:", test)
except TypeError:
    print("Error: The input list contains non-numeric elements.")
except NameError:
    print("Error: The 'lista' variable is not defined.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

""" EXPLANATION
lista was defined within the try block to prevent a NameError if it's not defined.
Add exception handling for TypeError to catch and handle the case where the list contains non-numeric elements.
Include a generic Exception catch-all to handle unexpected errors, providing a more informative error message.
 """