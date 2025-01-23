while(True):
    try:
        numbers = []
        size = int(input("Size of the List : "))
        items = 0

        while(size > items):
            num = int(input(f"Enter Number {items + 1} : "))
            numbers.append(num)
            items += 1

        numbers2 = []
        for num in numbers:
            if num % 2 == 0:
                numbers2.append(num)

        print("------------------------------")        
        print(f"Original List : {numbers}")
        print(f"Even Numbers List : {numbers2}")
        print("------------------------------")
        
    except:
        print("Something went wrong! Please try agian.")


