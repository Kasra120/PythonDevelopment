while(True):
    light = input("Traffic light color (Red/Yellow/Green) : ").strip().lower()

    if(light == "red"):
        print("Stop!")
    elif(light == "yellow"):
        print("Ready to Move!")
    elif(light == "green"):
        print("Move!")
    else:
        print("Invalid Input!")      