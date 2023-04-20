def calc(operator, x, y):       

    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "**":
        return x ** y
    elif operator == "%":
        if y==0:
             return print("niemoźna dzielić przez 0")
        else:
            return x % y
    
    elif operator == "*":
        return x * y
    elif operator == "/":
       if y == 0:
            return print("niemoźna dzielić przez 0")
       else:
            return x / y
       
    else:
        return None

def calc(figura , x, y):       

    if figura == "kwadrat":
        return x + y
    elif figura == "prostokąt":
        return x - y
    elif figura == "**":
        return x ** y
    elif figura == "%":
        return x ** y
       
    else:
        return None
print("podaj figurę")    
P=input()

print("podaj x") 

print("podaj y") 
y=int(input())

print(calc(figura, x, y))