# 2.1 - The two lines of code print the same output. The second line uses two strings separated by coma
print("Hello World!")
print("Hello", "World!")

# 2.2 - The first line prints an integer literal and the second one prints a floating-point literal
print(3)
print(3.0)

""" 2.3 - Same difference than the exercise above. Python prints integers as an integers and floating-point as a
floating-point."""
print(2 + 3)
print(2.0 + 3.0)

# 2.4 - The first line of code uses the multiplication operator and the second line uses the power operator
print(2 * 3)
print(2 ** 3)

""" 2.5 - The first line of code uses integer division operator and the output will be an floating-point 
literal while the second one uses integer division and results in an integer which would be the closest 
integer less. 
"""
print(7 / 3)
print(7 // 3)


# 3

def main():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)


main()


# 4
def km_to_miles(km):
    miles = km * 0.62
    return miles


def main():
    km = float(input("Type the distance in kilometers: "))
    result = km_to_miles(km)
    print(km, "kilometers are equal to ", result, " miles")


main()


# 5
def main():
    for c in range(0, 101, 10):
        f = 9/5 * c + 32
        print("Celsius: ", c, "Fahrenheit: ", f)


main()
