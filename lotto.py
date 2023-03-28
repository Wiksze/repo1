import random

for q in range(6):
    print("wybiez numer od 1do 49")


liczby=[]
for i in range(6):
    los=random.randint(1, 49)
    print(f"wylosowana liczba nr{i+1}")
    if los in liczby:
        los=random.randint(1, 49)
    print (los)
    liczby.append(los)

    

liczby = [1,4,2,6,7]
typy = set([1,2,3,4,5])
trafione = set(liczby) & typy
if trafione:
   print(len(trafione))

print(trafione)