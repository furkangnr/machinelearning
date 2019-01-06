def main():
    print ("Guess a number between 1 and 100")
    Number = int(42)
    found = False  # flag variable
    i = 0
    while not found and i < 10:
        userGuess = input("Your guess: ")
        if int(userGuess) == Number:
            print( "You got it !")
            found = True
        else:
            print("That is not it!")
        i +=1

if __name__ == "__main__":
    print("Hi!")
    main()




