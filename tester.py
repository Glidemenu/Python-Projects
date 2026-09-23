import random
import string
import time
import secrets
amount = int(input("How many letters do you want in your password? "))
user = int(input("How many letters do you want in your username? "))
letters = ''.join(random.choice(string.ascii_letters) for _ in range(amount))
username = ''.join(secrets.choice(string.ascii_letters) for _ in range(user))
print(f"Your username is {username}. And your password is {letters}")

input("press enter to exit")