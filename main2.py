# Functions 
def getNumeric (prompt):
    while True:
        response = input (prompt)
        try:
            return int (response)
        except ValueError:
                print ("Please enter a number.")

def play_again (prompt):
    while True:
        response = input (prompt).lower()
        if response == "yes":
            return True
        elif response == "no":
            print ("Goodbye!")
            return False
        else:
                print ("Please enter a valid answer, yes or no.\n")              
# main program 
play_game = True        
while play_game:
    numOne = getNumeric ("What is your first number?\n")
    numTwo = getNumeric ("What is your second number?\n")

    if numOne>numTwo:
      print ("Largest Number =" , numOne)

    elif numTwo>numOne:
      print ("Largest Number = ", numTwo)

    elif numOne==numTwo:
      print ("Both numbers are equal!")

    play_game = play_again ("Do you want to play again, yes or no?\n")
      