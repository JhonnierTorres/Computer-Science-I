import math


""" 1 - Chapter #2 - Discussion Problem #4(a,b,c,d) (pg. 4) """
print("*** CHAPTER 2 - Problem 4")
# a
for i in range(5):
    print(i * i)

# b
for d in [3, 1, 4, 1, 5]:
    print(d, end=" ")
# c
for i in range(4):
    print("Hello")
# d
for i in range(5):
    print(i, 2**i)

""" 2 - Chapter #3 - Discussion Problem #1(a,c,e) (pg. 77/78) """
print("*** CHAPTER 3 - Problem 1")
# a
num1 = float(4.0 / 10.0 + 3.5 * 2)
print(num1)

# c
num2 = int(abs(4 - 20 // 3)) ** 3
print(num2)

# e
num3 = int(3 * 10 // 3 + 10 % 3)
print(num3)

""" 3 - Chapter #3 - Discussion Problem #2(b,c) (pg. 78) """
print("*** CHAPTER 3 - Problem 2")
# b
n = 1
result_1 = (n * (n - 1)) / 2
print(result_1)

# c
r = 1.0
a = math.radians(1.0)
b = math.radians(1.0)

result_2 = math.sqrt(r * (math.cos(a)**2) + r * (math.sin(b)**2))

""" Chapter #3 - Discussion Problem #4(b,c) (pg. 78/79) """
print("*** CHAPTER 3 - Problem 4 ***")
# b
for i in [1, 3, 5, 7, 9]:
    print(i, ":", i**3)
print(i)

# c

x = 2
y = 10
for j in range(0, y, x):
    print(j, end="")
    print(x + y)
print("done")

""" Chapter #3 - Programming Exercise #6 (pg. 80) """

x1 = float(input("Enter the first x-coordinate: "))
y1 = float(input("Enter the first y-coordinate: "))
x2 = float(input("Enter the second x-coordinate: "))
y2 = float(input("Enter the second y-coordinate: "))

# slope
if x2 - x1 != 0:  # Ensure that the line is non-vertical
    slope = (y2 - y1) / (x2 - x1)
    print(f"The slope of the line through the two points is: {slope}")
else:
    print("The line is vertical, and the slope is undefined.")


""" Chapter #3 - Programming Exercise #7 (pg. 80) """
print("Now we are finding the distance between two points")
x1 = float(input("Enter the first x-coordinate: "))
y1 = float(input("Enter the first y-coordinate: "))
x2 = float(input("Enter the second x-coordinate: "))
y2 = float(input("Enter the second y-coordinate: "))

# distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between the two points is: {distance}")