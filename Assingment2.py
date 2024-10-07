"""
TASK 1:
You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
"""

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) >= 100 else "conference room"
print(venue)


"""
TASK 2:
Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.
"""

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if int(attendees) >= 100 else "conference room"
print(venue)
add_ons = (
    (
        "Okay projector included"
        if input("Would you like to add a projector? (yes/no): ") == "yes"
        else "No projector then"
    )
    if attendees > 100
    else (
        "Okay audio system included"
        if input("Would you like to add an audio system? (yes/no): ") == "yes"
        else "No audio then"
    )
)
print(add_ons)


"""
TASK 3:
Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
"""

vegetarian = input("Do you want vegetarian food? (yes/no): ")
caterer = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print("We recommend: " + caterer)
