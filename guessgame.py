n=18
numofgs=1
print("Number of guesses is limited i.e 6 times only: ")
while (numofgs<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(numofgs,"no.of guesses he took to finish.")
        break
#subtracting here
    print(9-numofgs,"no. of guesses left")
    numofgs = numofgs + 1

if(numofgs>9):
    print("Game Over")