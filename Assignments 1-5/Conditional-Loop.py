def askHowDay():
    question = input("Is today going to be a great day? Yes/No").capitalize()
    if question == "Yes":
        for question in range(10):
            print("Of course it is!")
    elif question == "No":
        print("Think more positively")
    else:
        print("Sorry please reinput I didn't understand")

askHowDay()