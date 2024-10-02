secret_number = 2
guess_limit = 3
i = 0
out_of_guesses = False

while i < guess_limit and not out_of_guesses:
    try:
        your_number = int(input("Enter your number: "))  
    except ValueError:
        print("Please enter a valid number!")
        continue  # Skip the rest of the loop if input is not a number

if your_number == secret_number:
    print("You won!")
    break  # Exit the loop if the guess is correct
else:
    i += 1
    if i == guess_limit:
        out_of_guesses = True
if out_of_guesses:
    print("Sorry, no guesses left!")
