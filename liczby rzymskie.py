
jednosci = ["", "I", "II", "III", "IV", "V", "VI", "VII", "IIX", "IX"]
dziesiatki = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "XXC", "CX"]
setki = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "CCM", "CM"]
tys = ["","M","MM","MMM","Mↁ","ↁ","ↁM","ↁMM","ↁMMM"]
dtys = ["","ↂ ","ↂ ↂ ","ↂ ↂ ↂ "]

print("tylko liczby mniejsze od 30000!")
cyfry = input("podaj liczbę\n")
while len(cyfry) < 5:
	cyfry = "0" + cyfry
	print(cyfry)


print (dtys[int(cyfry[-5])] + tys[int(cyfry[-4])] + setki[int(cyfry[-3])] + dziesiatki[int(cyfry[-2])] + jednosci[int(cyfry[-1])])




   