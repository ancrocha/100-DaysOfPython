from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()

tim.shape("turtle")
tim.color("aqua")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)


# exercise 2
# for _ in range(50):
#     tim.pd()
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)

# Exercoise 3
# for i in range(3, 10):

#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     sides = i
#     angle = 360 / sides

#     for side in range(sides):
#         tim.pencolor((r, g, b))
#         tim.forward(100)
#         tim.right(angle)


# Exercise 4

# tim.pensize(10)
# tim.speed(8)

# direction = [0, 90, 180, 270]

# for _ in range(200):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.pencolor((r, g, b))

#     tim.setheading(random.choice(direction))
#     tim.forward(30)


# Exercise 5

tim.speed("fastest")
for _ in range(int(360 / 15)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor((r, g, b))
    tim.circle(100)
    tim.right(15)


screen = Screen()
screen.colormode(255)
screen.exitonclick()
