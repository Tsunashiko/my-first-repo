"""
Script asks user if today is a good day and includes function to print iteration x-10
"""

def send__message():
    """
    Prints positive message 10 times
    """
    for question in range(10):
            print("Of course it is!")

question = input("Is today going to be a great day? Yes/No").capitalize()

if question == "Yes":
        send__message()

elif question == "No":
    print("Think more positively")

else:
    print("Sorry please reinput I didn't understand")

