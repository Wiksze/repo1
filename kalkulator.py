
def calc(operator, x, y):       

    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
       if y == 0:
            return print("niemoźna dzielić przez 0")
       else:
            return x / y
       
    else:
        return None
print("podaj x")    
x=int(input())
print("podaj operator") 
operator=input()
print("podaj y") 
y=int(input())

print(calc(operator, x, y))