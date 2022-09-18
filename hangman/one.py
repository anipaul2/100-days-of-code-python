import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter?").lower()
for letters in chosen_word:
    if letters == guess:
        print("Right")
    else:
        print("Wrong")