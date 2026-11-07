# Kiavash Niknam
import turtle
import random

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Chaos Game - Sierpinski Triangle")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Define triangle vertices
R = (-300, -250)
G = (300, -250)
B = (0, 270)

# Draw triangle
t.penup()
t.goto(R)
t.pendown()

t.color("black")
t.pensize(2)

t.goto(G)
t.goto(B)
t.goto(R)

# Define vertices and colors
vertices = [
    (R, "red"),
    (G, "green"),
    (B, "blue")
]

# Get number of iterations
n = int(input("Enter number of iterations: "))

# Starting point
x, y = R

t.penup()

# Chaos Game algorithm
for i in range(n):
    point, color = random.choice(vertices)

    x = (x + point[0]) / 2
    y = (y + point[1]) / 2

    t.goto(x, y)
    t.dot(4, color)

# Finish
turtle.done()
