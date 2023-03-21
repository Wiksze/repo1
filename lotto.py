for q in range(6):
    print("wybiez numer od 1do 49")
import random
liczby=[]
for i in range(6):
    los=random.randint(1, 49)
    print(f"wylosowana liczba nr{i+1}")
    if los in liczby:
        los=random.randint(1, 49)
    print (los)
    liczby.append(los)

    

