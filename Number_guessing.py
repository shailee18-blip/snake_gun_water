#Number guessing game
import random
attempts=0
secret=random.randint(1,100)
print("Think of a numbr btw 1 to 100 in 5 guesses")
while attempts<5:
    attempts+=1
    guess = int(input("Enter your guess: "))
    if guess<secret:
        print("Enter higher number")
    elif guess>secret:
        print("Enter lower number")
    else:
        print(f"Congratulations!!You guessed the number in {attempts}attempts")   
        break     
if attempts>=5:
    print(f"Better luck next time!You have finished your {attempts} attempts.")
