
jednosci = ["", "I", "II", "III", "IV", "V", "VI", "VII", "IIX", "IX"]
dziesiatki = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "XXC", "CX"]
setki = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "CCM", "CM"]
tys = ["M","MM","MMM","Mↁ","ↁ","ↁM","ↁMM","ↁMMM"]
dtys =int["ↂ"]

cyfry = input("podaj liczbę\n")
while len(cyfry) < 4:
	cyfry = "0" + cyfry
print (cyfry[int(cyfry[-5])] * "ↂ" + tys[int(cyfry[-4])] + setki[int(cyfry[-3])] + dziesiatki[int(cyfry[-2])] + jednosci[int(cyfry[-1])])





