"""
TASK 1:
You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.
"""

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


"""
TASK 2:
Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

"""
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("you can see the path and you will live!")
    elif cave_action == "proceed in the dark":
        print("wHy the heck would you proceed in the dark? Now you will die. Goodluck.")

"""
TASK 3:
If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?
"""

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("you can see the path and you will live!")
    elif cave_action == "proceed in the dark":
        print("wHy the heck would you proceed in the dark? Now you will die. Goodluck.")
    else:
        pass
else:
    pass
