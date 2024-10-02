secret_number = 2
guess_limit = 3
i = 0
out_of_guesses = False

while i < guess_limit and not out_of_guesses:
    try:
        your_number = int(input("Enter your number: "))
        
        if your_number == secret_number:
            print("You won!")
            break  
        else:
            i += 1
            if i == guess_limit:
                out_of_guesses = True
    except ValueError:
        print("Please enter a valid number!")
        
if out_of_guesses:
    print("Sorry, no guesses left!")
