import math
def calc(figura):       

    if figura == "kwadrat":
        print("podaj a")
        a=int(input())
        return a * a
    elif figura == "prostokąt":
        print("podaj a")
        a=int(input())
        print("podaj b")
        b=int(input())
        return a * b
    elif figura == "trójkąt":
        print("podaj a")
        a=int(input())
        print("podaj h")
        h=int(input())
        return a * h / 2
    elif figura == "romb":
        print("podaj e")
        e=int(input())
        print("podaj f")
        f=int(input())
        return e * f / 2
    elif figura == "trapez":
        print("podaj a")
        a=int(input())
        print("podaj b")
        b=int(input())
        print("podaj h")
        h=int(input())
        return (a + b) * h / 2
    elif figura == "deltoid":
        print("podaj a")
        a=int(input())
        print("podaj b")
        b=int(input())
        return a * b
    elif figura == "koło":
        print("podaj r")
        r=int(input())
        return math.pi * r**2
    elif figura == "równoległobok":
        print("podaj a")
        a=int(input())
        print("podaj h")
        h=int(input())
        return a * h
    elif figura == "elipsa":
        print("podaj a")
        a=int(input())
        print("podaj b")
        b=int(input())
        return a * b * math.pi
    else:
        return None
print("podaj figurę")    
figura=input()

print(calc(figura))
