print("wprowadz imie")
imie = input() 
print("witaj")
pin=1111
if int (input("wprowadz pin"))==pin:
    print("dostep przynany.")
    import random
    konto=random.randint(1000, 10000)
    print(f"twoj stan konta wynosi {konto}")
else:  
    print("odmowa dostępu")
