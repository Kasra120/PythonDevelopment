Students = [
    {"firstName" : "Ardalan", "lastName" : "Mohammadi", "class" : "301"},
    {"firstName" : "Hosein", "lastName" : "Sadeghi", "class" : "301"},
    {"firstName" : "Kasra", "lastName" : "Jahedi", "class" : "301"},
    {"firstName" : "Pouya", "lastName" : "Kateb", "class" : "301"},
    {"firstName" : "Kamran", "lastName" : "Nezami", "class" : "301"}
]

def search():
    found = False
    name = input("Enter the name of student : ").capitalize()
    for student in Students:
        if(student["firstName"] == name):
            print("------------------------------")
            print(f"First Name : {student["firstName"]}\nLast Name : {student["lastName"]}\nClass : {student["class"]}")
            print("------------------------------")
            found =True
    if(not found):
        print("Student not found!")

while(True):
    search()