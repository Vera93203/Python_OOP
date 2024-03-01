''' *** This is OOP first step to make turtle and screen ***
import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle ()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

'''

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Footballer Name", ["Haland", "Mhabpee", "Ronaldo"])
table.add_column("Power", ["Left", "Right", "Header"])

print(table.align)

print(table)
