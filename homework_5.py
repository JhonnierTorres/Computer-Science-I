from graphics import *
import math


"""  Chapter #6 - Programming Exercise #1 (pg. 206) """
def verse(animal, sound):
    print(f"Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print(f"And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh!")
    print(f"With a {sound}, {sound} here and a {sound}, {sound} there.")
    print(f"Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.")
    print(f"Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n")

animals = [("cow", "moo"), ("dog", "bark"), ("tiger", "roar"), ("pig", "oink"), ("sheep", "baa")]

for animal, sound in animals:
    verse(animal, sound)

""" Do Programming Exercise #14 from Chapter #3 (pg. 81) """
def average(numbers):

  sum = 0
  count = 0

  for i in range(numbers):
    number = float(input("Enter a number: "))
    sum += number
    count += 1

  average = sum / count
  return average

numbers = int(input("Enter the number of numbers to enter: "))
average = average(numbers)
print("The average is: ", average)

""" Do Programming Exercise #8 from Chapter #4 (pg. 127) """
def line(win, x1, y1, x2, y2):
    line = Line(Point(x1, y1), Point(x2, y2))
    line.draw(win)

def midpoint(win, x1, y1, x2, y2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    midpoint = Point(midpoint_x, midpoint_y)
    midpoint.setFill("cyan")
    midpoint.draw(win)

def slope(dx, dy):
    if dx != 0:
        slope = dy / dx
        return slope
    else:
        return float('inf')

def distance(dx, dy):
    distance = math.sqrt(dx**2 + dy**2)
    return distance

win = GraphWin("Line Segment Information", 500, 500)
win.setCoords(0, 0, 500, 500)

message = Text(Point(250, 480), "Click on two points to define the line segment.")
message.draw(win)

p1 = win.getMouse()
p2 = win.getMouse()

line(win, p1.getX(), p1.getY(), p2.getX(), p2.getY())
midpoint(win, p1.getX(), p1.getY(), p2.getX(), p2.getY())

dx = p2.getX() - p1.getX()
dy = p2.getY() - p1.getY()
slope = slope(dx, dy)
distance = distance(dx, dy)

result_message = Text(Point(200, 20), f"Length: {distance:.2f}\nSlope: {slope}")
result_message.draw(win)

win.getMouse()
win.close()

""" Chapter #6 - Programming Exercise #12 """

def sumList(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum

lista = ([10, 6, 20, 23])
test = sumList(lista)
print("The test result i: ", test)

""" Last Exercise """
def get_some_strings(num_strings):
  strings = []

  for i in range(num_strings):
    string = input("Enter a string: ")
    strings.append(string)

  return strings

num_strings = int(input("How many strings are you going to enter? "))
strings = get_some_strings(num_strings)
print("The list of strings is:", strings)


