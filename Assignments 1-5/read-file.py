"""
Script to display informantion obtained from write-file.py
"""

def read_and_display_file(filename="hackme.txt"):
    try:
        with open(filename, "r") as file:
            print("Here is some info to hack: ")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exits")

read_and_display_file()