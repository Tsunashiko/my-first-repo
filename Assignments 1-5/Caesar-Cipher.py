"""
.PY file for encrypting and decrypting data using Caesar-Cipher
"""

#Caesar Cipher Function from reading material
def caesar_cipher(text, shift, decrypt=False):
    encrypted_text = ""
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text +=chr((ord(char)- shift_base +shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


#get values for message and shift value
secret_message= input("What is your secret message ")
shift_value=int(input("pick a number between 1 and 25 "))

#prints if the number is too high or low

if shift_value > 25:
    print("sorry that number is too high")
elif shift_value < 1:
    print("that number is too low")
else:
    print("awesome we got ur number")


encrypted_value = caesar_cipher(secret_message, shift_value)
print(f"Encrypted: {encrypted_value}")

#Question will contiune to ask for decryption and loop until correct answer
while True:
    decrypt_message=input("would you like to decrypt message? Y/N ").capitalize()
    if decrypt_message == "Y":
        decrypted_value = caesar_cipher(encrypted_value, shift_value, decrypt=True)
        print(f"Decrypted: {decrypted_value}")
        break
    elif decrypt_message == "N":
        print("Ok, but the message needs to be decrypted")

    else:
        print("I'm sorry I didn't understand your answer")


#moved everything I tried to use in my code that failed or wasn't working as intended to bottom


#turning shift value to function for error handling still WIP
"""def ShiftValueFunction():
    input("pick a number between 1 and 25 ")
    if int == str:
        print("that is not a number")
    elif int > 25:
        print("too high")
    elif int < 1:
        print("too low")
    else:
        print("awesome we got your number")"""


#function for making new shift value second attempt
"""
new_shift_value = 26 - shift_value
def caesar_cipher_decryption(text,shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text +=chr((ord(char)- shift_base +shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return     
print(caesar_cipher_decryption(encrypted_value, new_shift_value))
"""