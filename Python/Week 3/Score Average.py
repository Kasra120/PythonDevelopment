while(True):
    try:
        scores = []
        count = int(input("Count of the Scores : "))
        score = 0

        while(count > score):
            num = int(input(f"Enter Score {score + 1} : "))
            scores.append(num)
            score += 1
        
        sum = 0
        for num in scores:
            sum += num
        average = sum / count

        print("------------------------------")        
        print(f"List : {scores}")
        print(f"Sum of Scores : {sum}")
        print(f"Count of Scores : {count}")
        print(f"Average : {average}")
        print("------------------------------")
        
    except:
        print("Something went wrong! Please try agian.")