name = input("Insert your name here: ")
age = input("How old are you: ")
ageInt = int(age)

def future_age(a, b):
    return a + b

age2 = future_age(ageInt,2)

print("Hello", name)
print("today is going to be a great day!")
print("In 2 years, you will be ",age2," years old")

