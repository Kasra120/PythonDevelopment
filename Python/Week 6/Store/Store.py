import StoreModules as Modules
while(True):
    try:
        print("------------------------------")
        action = int(input("Menu :\n1.Add Product\n2.Find Product\n3.Delete Product\n4.Edit Product\nYour Choice : "))
        print("------------------------------")
        match action:
            case 1:
                name = input("Enter product name : ").capitalize()
                while (True):
                    try:
                        price = float(input("Enter product price : "))
                        break
                    except:
                        print("That's not an number! Please try again later.")
                product = Modules.Product(name, price)
                product.addProduct()
            case 2:
                name = input("Enter product name : ").capitalize()
                product = Modules.Product(name)
                product.findProduct()
            case 3:
                name = input("Enter product name : ").capitalize()
                product = Modules.Product(name)
                product.deleteProduct()
            case 4:
                name = input("Enter product name : ").capitalize()
                product = Modules.Product(name)
                newName = input("Enter product new name : ").capitalize()
                while (True):
                    try:
                        price = float(input("Enter product price : "))
                        break
                    except:
                        print("That's not an number! Please try again later.")
                newProduct = Modules.Product(newName, price)
                newProduct.editProduct(product)
            case _:
                print("Please choose an option!")
    except:
        print("------------------------------")
        print("Input not valid! Please try again.")
    finally:
        Modules.connection.close()