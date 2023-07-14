secret_number=2
your_number=input("enter your number")
i=0
guess_limit=3
out_of_guess=False
while your_number!=secret_number and not(out_of_guess):
    if i<guess_limit:
       your_number=input("enter your number")
       i=i+1
    else:
       out_of_guess=True
if out_of_guess:
    print("sorry no guess left")
else:
    print("you won")