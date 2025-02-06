Products = [
    {"name" : "Milk", "price" : 20.0, "VAT" : 2.0},
    {"name" : "Bread", "price" : 15.0, "VAT" : 1.5},
    {"name" : "Soda", "price" : 30.0, "VAT" : 3.0},
    {"name" : "Ice Cream", "price" : 25.0, "VAT" : 2.5},
    {"name" : "Chocolate", "price" : 10.0, "VAT" : 1.0},
]

def addProduct():
    name = input("Enter product name : ").capitalize()
    while(True):
        try:
            price = float(input("Enter product price : "))
            break
        except:
            print("That's not an number! Please try again later.")
    VAT = price / 10
    Products.append({"name" : name, "price" : price, "VAT" : VAT})
    print("Prodcut added succesfully.")
    
def findProduct():
    found = False
    name = input("Enter product name : ").capitalize()
    for product in Products:
        if(product["name"] == name):
            print(f"Product : {product["name"]}\nPrice : {product["price"]}\nVAT : {product["VAT"]}")
            found = True
    if(not found):
        print("Product not found!")

def deleteProduct():
    deleted = False
    name = input("Enter product name : ").capitalize()
    for product in Products:
        if(product["name"] == name):
            Products.remove(product)
            print("Prodcut deleted succesfully.")
            deleted = True
    if(not deleted):
        print("Product not found!")

def editProduct():
    found = False
    while(not found):
        name = input("Enter product name : ").capitalize()
        for product in Products:
            if(product["name"] == name):
                print("Product found! Enter new values.")
                found = True
                break
        if(not found):
            print("Product not found! Please try again.")
    newName = input("Enter product name : ").capitalize()
    while(True):
        try:
            price = float(input("Enter product price : "))
            break
        except:
            print("That's not an number! Please try again later.")
    VAT = price / 10
    Products.remove(product)
    Products.append({"name" : newName, "price" : price, "VAT" : VAT})

while(True):
    try:
        print("------------------------------")
        action = int(input("Menu :\n1.Add Product\n2.Find Prodcut\n3.Delete Product\n4.Edit Product\nYour Choice : "))
        print("------------------------------")
        if(action == 1):
            addProduct()
        elif(action == 2):
            findProduct()
        elif(action == 3):
            deleteProduct()
        elif(action == 4):
            editProduct()
    except:
        print("------------------------------")
        print("Input not valid! Please try again.")