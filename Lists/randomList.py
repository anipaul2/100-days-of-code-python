import random
from tkinter import N
names = input("Drop some names ")
split_names = names.split(", ")

# person_who_will_pay = random.choice(split_names)
# print(person_who_will_pay + " is going to buy the meal today!")

person_who_will_pay = random.randint(0, len(split_names) - 1)
name_of_the_person = split_names[person_who_will_pay]
print(name_of_the_person + " is going to pay for the food!")
