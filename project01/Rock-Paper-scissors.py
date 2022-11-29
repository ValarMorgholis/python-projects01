import random
import time

player1 = input(
    "First player please choice your weapons (rock & papaer & scissors) : ").lower()

computer = random.randint(0, 2)
print("Computer is choice her weapon - - - - ")
time.sleep(3)


if computer == 0:
    computer = 'r'
elif computer == 1:
    computer = 'p'
elif computer == 2:
    computer = 's'

r = ['r', "rock"]  # rock
p = ['p', "paper"]  # paper
s = ['s', "scissors"]  # scissors


if player1 == computer:
    print(f"No one won, both was the same.")

elif player1 == r[0]:

    if computer == p[0]:
        print(f"Second player won, first was {r[1]} and second was {p[1]}")

    elif computer == s[0]:
        print(f"Second player won, first was {r[1]} and second was {s[1]}")

# __________________________________________________

elif player1 == p[0]:

    if computer == r[0]:
        print(f"First player won, first was {p[1]} and second was {r[1]}")

    elif computer == s[0]:
        print(f"Second player won, first was {p[1]} and second was {s[1]}")

# __________________________________________________


elif player1 == s[0]:

    if computer == r[0]:
        print(f"First player won, first was {p[1]} and second was {r[1]}")

    elif computer == p[0]:
        print(f"Second player won, first was {p[1]} and second was {s[1]}")
else:
    print("You entered worng input")
    
