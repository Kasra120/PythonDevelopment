import StoreModules as Modules
while(True):
    try:
        print("------------------------------")
        action = int(input("Menu :\n1.Add Product\n2.Find Prodcut\n3.Delete Product\n4.Edit Product\nYour Choice : "))
        print("------------------------------")
        match action:
            case 1:
                Modules.addProduct()
            case 2:
                Modules.findProduct()
            case 3:
                Modules.deleteProduct()
            case 4:
                Modules.editProduct()
            case _:
                print("Please choose an option!")
    except:
        print("------------------------------")
        print("Input not valid! Please try again.")
    finally:
        Modules.connection.close()