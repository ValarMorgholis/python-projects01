input1 = input(
    "First player please choice your weapons (rock & papaer & scissors) : ")

input2 = input(
    "Second player please choice your weapons (r & p & s) : ")

r = ['r', "rock"]  # rock
p = ['p', "paper"]  # paper
s = ['s', "scissors"]  # scissors


if input1 == r[0] and input2 == r[0]:
    print(f"No one won, both was {r[1]}.")

elif input1 == r[0] and input2 == p[0]:
    print(f"Second player won, first was {r[1]} and second was {p[1]}")

elif input1 == r[0] and input2 == s[0]:
    print(f"First player won, first was {r[1]} and second was {s[1]}")

# __________________________________________________

if input1 == p[0] and input2 == p[0]:
    print(f"No one won, both was {p[1]}.")

elif input1 == p[0] and input2 == r[0]:
    print(f"Second player won, first was {p[1]} and second was {r[1]}")

elif input1 == p[0] and input2 == s[0]:
    print(f"First player won, first was {p[1]} and second was {s[1]}")

# __________________________________________________


if input1 == s[0] and input2 == s[0]:
    print(f"No one won, both was {s[1]}.")

elif input1 == s[0] and input2 == r[0]:
    print(f"Second player won, first was {s[1]} and second was {r[1]}")

elif input1 == s[0] and input2 == p[0]:
    print(f"First player won, first was {s[1]} and second was {p[1]}")

else:
    print("You entered worng input")