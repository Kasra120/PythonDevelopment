while(True):
    try:
        score = int(input("Enter Score : "))
        if(score >= 90 and score <= 100):
            print("Perfect!")
        elif(score >= 70 and score < 90):
            print("Good!")
        elif(score >= 50 and score < 70):
            print("Need More Effort!")
        elif(score >= 0 and score < 50):
            print("Failed!")
        else:
            print("Invalid Score! Please try again.")
    except:
        print("Invalid Input! Please try again.")