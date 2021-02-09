from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? red, blue, yellow, green or orange: ")
colors = ["red", "blue", "green", "yellow", "orange"]
y_position = [0, 50, -50, 100, -100]
all_turtles =[]

for turtle_index in range(0, 5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                screen.title(f"You have won! The {winning_turtle} turtle is the winner.")

            else:
                screen.title(f"You have lost. The {winning_turtle} turtle is the winner.")

        number = random.randint(0, 10)
        turtle.fd(number)

screen.exitonclick()

