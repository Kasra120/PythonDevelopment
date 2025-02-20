import math

def Add(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def Subtract(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")

def Multiply(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}")

def Divide(num1, num2):
    print(f"{num1} / {num2} = {num1 / num2}")

def Power(num1, num2):
    print(f"{num1} ^ {num2} = {pow(num1, num2)}")
    
def Squareroot(num1):
    print(f"√{num1} = {math.sqrt(num1)}")

def Sine(num1):
    print(f"Sin {num1} = {math.sin(math.radians(num1))}")

def Cosine(num1):
    print(f"Cos {num1} = {math.cos(math.radians(num1))}") 

def Tangent(num1):
    print(f"Tan {num1} = {math.tan(math.radians(num1))}") 

def Cotangent(num1):
    print(f"Cot {num1} = {(1 / math.tan(math.radians(num1)))}") 