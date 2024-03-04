import turtle as t
import random
from turtle import Screen, Turtle  # Import the Turtle class

Tim = t.Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shapesize(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        Tim.forward(100)
        Tim.right(angle)

def draw_labeled_shapes():
    for shape_side in range(3, 11):
        Tim.color(random.choice(colors))
        draw_shapesize(shape_side)
        Tim.penup()
        Tim.forward(120)  # Move to the right for the next shape
        Tim.pendown()
        Tim.write(f"{shape_side} sides", align="center", font=("Arial", 10, "normal"))
        Tim.penup()
        Tim.backward(120)  # Move back to the starting position for the next iteration
        Tim.pendown()

# Set up the screen and label turtle
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("PMM's Different Shapes")

label_turtle = Turtle()
label_turtle.hideturtle()
label_turtle.penup()
label_turtle.goto(0, 300)  # Adjust the position to be more towards the top
label_turtle.color("white")
label_turtle.write("မန်ဃူဖန်တွေလီးပဲ🫶🏻", align="center", font=("Arial", 25, "normal"))  # Increase font size

# Draw labeled shapes
draw_labeled_shapes()

t.done()
