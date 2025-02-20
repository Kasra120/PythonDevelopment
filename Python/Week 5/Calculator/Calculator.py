import MathModules as Modules

while(True):
    try:
        print("------------------------------")
        action = int(input("Menu :\n1.Add\t\t2.Subtract\n3.Multiply\t4.Divide\n5.Power\t\t6.Square Root\n7.Sine\t\t8.Cosine\n9.Tangent\t10.Cotangent\nYour choice : "))
        print("------------------------------")
        match action:
            case 1:
                num1 = float(input("Enter the first number : "))
                num2 = float(input("Enter the second number : "))
                Modules.Add(num1,num2)
            case 2:
                num1 = float(input("Enter the first number : "))
                num2 = float(input("Enter the second number : "))
                Modules.Subtract(num1,num2)
            case 3:
                num1 = float(input("Enter the first number : "))
                num2 = float(input("Enter the second number : "))
                Modules.Multiply(num1,num2)
            case 4:
                num1 = float(input("Enter the first number : "))
                num2 = float(input("Enter the second number : "))
                Modules.Divide(num1,num2)
            case 5:
                num1 = float(input("Enter the number : "))
                num2 = float(input("Enter the power : "))
                Modules.Power(num1, num2)
            case 6:
                num1 = float(input("Enter the number : "))
                Modules.Squareroot(num1)
            case 7:
                num1 = float(input("Enter the number : "))
                Modules.Sine(num1)
            case 8:
                num1 = float(input("Enter the number : "))
                Modules.Cosine(num1)
            case 9:
                num1 = float(input("Enter the number : "))
                Modules.Tangent(num1)
            case 10:
                num1 = float(input("Enter the number : "))
                Modules.Cotangent(num1)   
            case _:
                print("Please choose an action!")
    except:
        print("------------------------------")
        print("That's not an number! Please try again.")