"""
Script for cracking passwords from shadow 512 using brute force
"""

from passlib.hash import sha512_crypt



SHADOW_FILE = r'/home/justincase/Desktop/my-first-repo/Assignments 1-5/shadow.txt'
PASSWORD_FILE = r'/home/justincase/Desktop/my-first-repo/Assignments 1-5/passwords.txt'

def guess_password(shadow_file, password_file):
    successful_attempts = []

    try:
        with open(shadow_file, 'r', encoding='utf-8') as sf, open(password_file, 'r', encoding='utf-8') as pf:
            shadows = sf.readlines()
            passwords = [pw.strip() for pw in pf.readlines()]


            for shadow in shadows:
                parts = shadow.split(":")
                if len(parts) < 2 or '!' in parts [1] or '*' in parts [1]:
                    continue
                username, hash_password = parts[0], parts[1].strip()

                for password in passwords:
                    try:
                        if sha512_crypt.verify(password, hash_password):
                            successful_attempts.append((username, password))
                            print(f'[+] Cracked {username}: {password}')
                            break
                    except ValueError:
                        continue


    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    if successful_attempts:
        print("\n=== Cracked Password ===")
        for username, password in successful_attempts:
            print(f'User: {username}, Password: {password}')
    else:
        print("\nNo Passwords were found or cracked")


#Run the function
guess_password(SHADOW_FILE, PASSWORD_FILE)
