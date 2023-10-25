from graphics import *

""" Chapter #3 - Programming Exercise #13 (pg. 81) """

numbers = int(input("How many numbers would you like to sum?: "))
result = 0

for i in range(numbers):
    number = int(input("Enter a number: "))
    result += number

print("The result is: ", result)

""" Chapter #3 - Programming Exercise #14 (pg. 81) """

numbers2 = int(input("Enter the number of numbers to be averaged: "))
result2 = 0

for i in range(numbers2):
    number = float(input(f"Enter number {i + 1}: "))
    result2 += number

average = result2 / numbers2
print("The average is: ", average)

""" Chapter #4 - Discussion Problem #2(a,b,c,d,e,f,g) (pg. 125) """
# a
point = Point(130, 130)
win = GraphWin("Tittle", 800, 800)
point.draw(win)
""" The outcome of this is a single point at the coordinates (130, 130) """

# b
c = Circle(Point(30, 40), 25)
c.setFill("blue")
c.setOutline("red")
c.draw(win)
"""The outcome is a circle object centered at (30, 40) and with a radius of 25 pixels. 
This circle is filled with blue and has a red outline."""

# c
r = Rectangle(Point(20, 20), Point(40, 40))
r . setFill(color_rgb(0, 255, 150))
r . setWidth(3)
r.draw(win)
""" A rectangle that has a top-left corner at (20, 20) and a bottom-right corner at (40, 40). 
This object is filled with color_rgb(0, 255, 150) and has a 3-pixel wide outline. """

# d
li = Line(Point(100, 100), Point(100, 200))
li.setOutline("red4")
li.setArrow("first")
li.draw(win)
""" The outcome is a red line that has an arrowhead at the start of the line. 
The line starts at (100, 100) and ends at (100, 200)"""

# e
oval = Oval(Point(50, 50), Point(60, 100))
oval.draw(win)
""" The outcome is an oval that has a top-left corner at (50, 50) and a bottom-right corner at (60, 100). """
# f
shape = Polygon(Point(5, 5), Point(10, 10), Point(5, 10), Point(10, 5))
shape.setFill("orange")
shape.draw(win)
""" The outcome is a polygon with four vertices: (5,5), (10,10), (5,10), and (10,5). This is filled with orange """

# g
t = Text(Point(100, 100), "Hello World! ")
t.setFace("courier")
t.setSize(16)
t.setStyle("italic")
t.draw(win)
win.getMouse()
win.close()
""" The outcome is a text saying "Hello World!". It is in the Courier font, size 16, and italicized. 
The text is positioned at the coordinates (100, 100). """

""" Chapter #4 - Discussion Problem #3 (pg. 128) """

w = GraphWin("Problem 3", 800, 800)
shape = Circle(Point(50, 50), 20)
shape.setOutline("red")
shape.setFill("red")
shape.draw(w)
for i in range(10):
    p = w.getMouse()
    c = shape.getCenter()
    dx = p.getX() - c.getX()

w.close()

""" This program is a simple interactive graphics program that allows the user to move a red circle
around the screen with the mouse. The program first creates a graphics window and then draws 
a red circle in the center of the window. Then, it enters a loop that runs 10 times. In each iteration
of the loop, the program gets the current mouse position and the center of the circle. 
It then calculates the difference in the x-coordinates of the two points. If the difference is positive,
the program moves the circle to the right by the amount of the difference. If the difference is negative,
the program moves the circle to the left by the amount of the difference. After moving the circle,
the program redraws it in the window. """

""" Chapter #4 - Programming Exercise #2 (pg. 126) """

target_radius = 400
ring = target_radius // 5

wi = GraphWin("Archery Target", target_radius * 2, target_radius * 2)

yellow_circle = Circle(Point(target_radius, target_radius), target_radius)
yellow_circle.setFill("yellow")
yellow_circle.draw(wi)

colors = ["red", "blue", "black", "white"]
for i in range(len(colors)):
    ring2 = Circle(Point(target_radius, target_radius), target_radius - (i + 1) * ring)
    ring2.setFill(colors[i])
    ring2.draw(wi)

wi.getMouse()
wi.close()

""" Chapter #4 - Programming Exercise #3 (pg. 126) """

win3 = GraphWin("Face", 400, 400)

# head
head = Circle(Point(100, 100), 40)
head.setFill("yellow")
head.setOutline("black")
head.draw(win3)

# eyes
left_eye = Circle(Point(85, 85), 3)
left_eye.setFill("black")
left_eye.draw(win3)

right_eye = Circle(Point(115, 85), 3)
right_eye.setFill("black")
right_eye.draw(win3)

# smile
smile = Line(Point(85, 110), Point(115, 110))
smile.setWidth(2)
smile.draw(win3)

win3.getMouse()
win3.close()

""" Chapter #4 - Programming Exercise #8 (pg. 126) """

win2 = GraphWin("Exercise 8", 400, 400)
# endpoints from the clicks
p1 = win2.getMouse()
p2 = win2.getMouse()

# Draw the line
line = Line(p1, p2)
line.draw(win2)

# midpoint
midpoint = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)

# length
dx = p2.getX() - p1.getX()
dy = p2.getY() - p1.getY()
length = (dx ** 2 + dy ** 2) ** 0.5

# slope
slope = dy / dx if dx != 0 else "undefined"

# midpoint in cyan
midpoint.setFill("cyan")
midpoint.draw(win2)

# Final Information
Text(Point(200, 20), f"Midpoint: ({midpoint.getX()}, {midpoint.getY()})").draw(win2)
Text(Point(200, 40), f"Length: {length:.2f} units").draw(win2)
Text(Point(200, 60), f"Slope: {slope}").draw(win2)

win2.getMouse()
win2.close()
