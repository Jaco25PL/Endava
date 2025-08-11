import random 

secret_number = random.randint(1, 10)
tries = 0
guessed = False

print("Guess the secret number between 1 and 10")

while not guessed:
    your_try = int(input("Your number: "))
    if your_try == secret_number:
        print(f"You got it! Number {secret_number} in {tries} tries")
        guessed = True
        # break
    elif your_try < secret_number:
        print("Try higher")
    else:
        print("Try lower")
    tries += 1

