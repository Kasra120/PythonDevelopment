while(True):
    password = "kasra120"
    guessCount = 3
    while (True):
        guess = input(f"Enter your guess. You have {guessCount} chances : ")
        if(guess == password):
            print("Congratulations! You Win!")
            break
        else:
            guessCount -= 1
            if(guessCount == 0 ):
                print("GameOver! You Lose!")
                break
            print("Wrong guess! Try again.")