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
        for num in numbers2:
            if(numbers2.count(num) > 1):
                numbers2.remove(num)

        print("------------------------------")        
        print(f"Original List : {numbers}")
        print(f"List Without Duplicate Numbers : {numbers2}")
        print("------------------------------")

    except:
        print("Something went wrong! Please try agian.")