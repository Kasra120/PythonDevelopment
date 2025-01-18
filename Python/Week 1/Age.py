while (True):
    try:
        year = int(input("Your Birth Year : "))
        if(year > 1403 or year < 1250):
            print("Error! Please try again.")
        else:
            print(f"Your Age : {1403 - year}")
    except:
        print("Thats not a number! Please try again.")