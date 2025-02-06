def averageCalc():
    average = 0
    size = 0
    scores = []
    i = 0

    while (size <= 0):
        try:
            size = int(input("Enter count of the scores : "))
        except:
            print("That's not an number! Please try again later.")

    while(i < size):
        try:
            score = float(input(f"Enter Score {i+1} : "))
            scores.append(score)
            i += 1
        except:
            print("That's not an number! Please try again later.")
            
    for score in scores:
        average += score
    average /= len(scores)
    print("------------------------------")
    print(f"Average of the Scores : {average}")
    print("------------------------------")

while(True):
    averageCalc()