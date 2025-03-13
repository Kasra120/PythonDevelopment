import sqlite3
connection = sqlite3.connect("StoreDB.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Products(Product text NOT NULL, Price INTEGER NOT NULL, VAT INTEGER NOT NULL)")
connection.close()

class Product:
    def __init__(self, product, price=0):
        self.product = product
        self.price = price
        self.vat = price / 10

    def addProduct(self):
        connection = sqlite3.connect("StoreDB.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Products VALUES(?, ?, ?)",(self.product, self.price, self.vat))
        connection.commit()
        connection.close()
        print("Product added successfully.")

    def findProduct(self):
        found = False
        connection = sqlite3.connect("StoreDB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Products WHERE Product = ?",(self.product,))
        result = cursor.fetchone()
        connection.close()
        if(result):
            print(f"Product : {result[0]}\nPrice : {result[1]}\nVAT : {result[2]}")
        else:
            print("Product not found!")

    def deleteProduct(self):
        deleted = False
        connection = sqlite3.connect("StoreDB.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Products WHERE Product = ?",(self.product,))
        deleted = connection.commit()
        connection.close()
        print("Product deleted successfully.")
        if(deleted):
            print("Product not found!")

    def editProduct(self,other):
        found = False
        while(not found):
            connection = sqlite3.connect("StoreDB.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Products WHERE Product = ?",(other.product,))
            found = cursor.fetchone()
            connection.close()
            if(not found):
                print("Product not found! Please try again.")
            else:
                found = True
        VAT = self.price / 10
        connection = sqlite3.connect("StoreDB.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE Products SET Product = ?, Price = ?, VAT = ? WHERE Product = ?",(self.product, self.price, VAT, other.product))
        connection.commit()
        connection.close()
        print("Product updated successfully.")
