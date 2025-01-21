"""
Script that will ask user for name, favorite color, pets name, mothers maiden name, and elementary school
"""

def collect_user_data():
    print("Please answer the following questions")
    name = input("name? ")
    favorite_color = input("Favorite Color? ") 
    first_pet = input("First pets name? ")
    mothers_maiden_name = input("Mother's maiden name? ")
    elementary_school = input("Elementary School? ")

    return {
        "Name":name,
        "Favorite Color":favorite_color,
        "First Pet":first_pet,
        "Mother's Maiden Name":mothers_maiden_name,
        "Elementary School":elementary_school

    }


def save_to_file(data, filename="hackme.txt"):
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"Info has been saved to {filename}.")


save_to_file(collect_user_data())

