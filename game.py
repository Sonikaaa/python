secret_word="hi"
word=input("enter your word ")
i=1
while word!=secret_word: 
    if i<3:
     word=input("enter your word ")
     i=i+1
    else:
      print("you lost")
      break
if word==secret_word:
 print("correct")