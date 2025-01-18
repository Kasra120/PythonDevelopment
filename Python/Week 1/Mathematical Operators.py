while(True):
    try:
        number1 = int(input("First Number : "))
        number2 = int(input("Second Number : "))
        print(f"{number1} + {number2} = {number1 + number2}")
        print(f"{number1} - {number2} = {number1 - number2}")
        print(f"{number1} * {number2} = {number1 * number2}")
        print(f"{number1} / {number2} = {number1 / number2}")
    except:
        print("Something went wrong! Please try again.")