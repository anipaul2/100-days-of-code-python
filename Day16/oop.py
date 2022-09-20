from turtle import Turtle, Screen
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

ans = Turtle()
print(ans)
ans.shape("turtle")
ans.color("coral")
ans.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


