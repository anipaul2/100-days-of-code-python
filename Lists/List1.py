states_in_india = ["Assam", "Manipur", "Gujurat", "Karnataka"]
print(states_in_india[1])
print(states_in_india[0])
# In python square brackets means lists
print(states_in_india[-1])

#you can changes the data too
states_in_india[1] = "Shillong"
print(states_in_india)

#you can also add a new string in the end of the list
states_in_india.append("Sikkim")
print(states_in_india)

# You can extend the list too by adding a new list
states_in_india.extend(["Uttarkhand", "Imphal", "Sikkim"])
print(states_in_india)