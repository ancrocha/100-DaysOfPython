# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import random
from turtle import Turtle, Screen
color_list = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165,
                                                                                                                                                                                                            157), (15, 96, 70), (58, 50, 47), (50, 111, 90), (49, 42, 47), (34, 61, 56), (227, 165, 169), (170, 188, 221), (184, 103, 112), (32, 59, 108), (105, 127, 160), (175, 200, 188), (33, 150, 210), (65, 66, 56)]

screen = Screen()
screen.colormode(255)

tim = Turtle()

tim.speed("fastest")

tim.pu()
tim.hideturtle()
x = -300.0
y = -300.0
tim.setpos(x, y)

for _ in range(10):

    for _ in range(10):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.forward(50)

    y += 50
    tim.setpos(x, y)

screen = Screen()
screen.colormode(255)
screen.exitonclick()
