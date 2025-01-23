while(True):
    try:
        numbers = []
        size = int(input("Size of the List : "))
        items = 0
        while(size > items):
            num = int(input(f"Enter Number {items + 1} : "))
            numbers.append(num)
            items += 1
        
        numbers2 = numbers[:]
        rotate = int(input("Number of times to rotate : "))
        roll = 0 
        while(rotate > roll):
            rolledNumber = numbers2.pop(0)
            numbers2.append(rolledNumber)
            roll+=1

        print("------------------------------")        
        print(f"Original List : {numbers}")
        print(f"Rotated List : {numbers2}")
        print("------------------------------")

    except:
        print("Something went wrong! Please try agian.")