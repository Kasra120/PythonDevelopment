import sqlite3
connection = sqlite3.connect("StoreDB.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Products(Product text NOT NULL, Price INTEGER NOT NULL, VAT INTEGER NOT NULL)")
connection.close()

def addProduct():
    name = input("Enter product name : ").capitalize()
    while(True):
        try:
            price = float(input("Enter product price : "))
            break
        except:
            print("That's not an number! Please try again later.")
    VAT = price / 10
    connection = sqlite3.connect("StoreDB.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Products VALUES(?, ?, ?)",(name, price, VAT))
    connection.commit()
    connection.close()
    print("Prodcut added succesfully.")
    
def findProduct():
    found = False
    name = input("Enter product name : ").capitalize()
    connection = sqlite3.connect("StoreDB.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products WHERE Product = ?",(name,))
    result = cursor.fetchone()
    connection.close()
    if(result):
        print(f"Product : {result[0]}\nPrice : {result[1]}\nVAT : {result[2]}")
    else:
        print("Product not found!")

def deleteProduct():
    deleted = False
    name = input("Enter product name : ").capitalize()
    connection = sqlite3.connect("StoreDB.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Products WHERE Product = ?",(name,))
    deleted = connection.commit()
    connection.close()
    print("Product deleted succesfully.")
    if(deleted):
        print("Product not found!")

def editProduct():
    found = False
    while(not found):
        name = input("Enter product name : ").capitalize()
        connection = sqlite3.connect("StoreDB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Products WHERE Product = ?",(name,))
        found = cursor.fetchone()
        connection.close()
        if(not found):
            print("Product not found! Please try again.")
        else:
            found = True
    newName = input("Enter product new name : ").capitalize()
    while(True):
        try:
            price = float(input("Enter product price : "))
            break
        except:
            print("That's not an number! Please try again later.")
    VAT = price / 10
    connection = sqlite3.connect("StoreDB.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Products SET Product = ?, Price = ?, VAT = ? WHERE Product = ?",(newName, price, VAT, name))
    connection.commit()
    connection.close()
    print("Product updated succesfully.")
