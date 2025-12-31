# Snake Water Gun
import random

select = ("snake", "water", "gun")
computer = random.choice(select)  # fixed

user = input("Enter choice [snake, water, gun]: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("It's a tie")

elif user == "snake" and computer == "water":
    print("User wins")
elif user == "water" and computer == "gun":
    print("User wins")
elif user == "gun" and computer == "snake":
    print("User wins")

elif user == "water" and computer == "snake":
    print("Computer wins")
elif user == "gun" and computer == "water":
    print("Computer wins")
elif user == "snake" and computer == "gun":
    print("Computer wins")

else:
    print("Invalid input")
