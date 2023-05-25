
jednosci = ["", "I", "II", "III", "IV", "V", "VI", "VII", "IIX", "IX"]
dziesiatki = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "XXC", "XC"]
setki = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "CCM", "CM"]
tys = ["","M","MM","MMM","Mↁ","ↁ","ↁM","ↁMM","ↁMMM","Mↂ "]
dtys = ["","ↂ ","ↂ ↂ ","ↂ ↂ ↂ "]
ilosc = 0

print("tylko liczby mniejsze od 40000!")
cyfry = (input("podaj liczbę\n"))
ilosc = cyfry

if int(ilosc) >= 40000:
	cyfry = (input("zbyt wysoka liczba\n Podaj liczbę jeszcze raz"))

while len(cyfry) < 5:
	cyfry = "0" + cyfry
	print (dtys[int(cyfry[-5])] + tys[int(cyfry[-4])] + setki[int(cyfry[-3])] + dziesiatki[int(cyfry[-2])] + jednosci[int(cyfry[-1])])
	print("\n---------------------------")