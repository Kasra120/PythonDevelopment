while(True):
    movie = input("Is your favorite movie playing? (Yes/No) : ").strip().lower()
    ticket = input("Are the tickets cheap? (Yes/No) : ").strip().lower()
    time = input("Do you have free time? (Yes/No) : ").strip().lower()

    if (movie == "yes" and ticket == "yes" and time == "yes"):
        print("Go to the Cinema!")
    else:
        print("Don't go to the Cinema!")