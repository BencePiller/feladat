# 5. feladat
def sorozat_vizsgalat():
	print("5. feladat: Számtani/mértani sorozat vizsgálat")
	a = float(input("Első szám: "))
	b = float(input("Második szám: "))
	c = float(input("Harmadik szám: "))
	if b - a == c - b:
		print("Számtani sorozat. Következő elem:", c + (b - a))
	elif b / a == c / b and a != 0 and b != 0:
		print("Mértani sorozat. Következő elem:", c * (b / a))
	else:
		print("Nem sorozat.")

# 6. feladat
def nev_kiiras():
	print("6. feladat: Név kiírása 10-szer")
	nev = input("Add meg a neved: ")
	print("A) Léptető ciklussal:")
	for _ in range(10):
		print(nev)
	print("B) Hátul tesztelő ciklussal:")
	i = 0
	while True:
		print(nev)
		i += 1
		if i >= 10:
			break
	print("C) Elöl tesztelő ciklussal:")
	i = 0
	while i < 10:
		print(nev)
		i += 1

# 7. feladat
def szamok_kiirasa():
	print("7. feladat: Számok kiírása 100-ig")
	print("A) Páros számok:")
	for i in range(2, 101, 2):
		print(i, end=" ")
	print("\nB) Páratlan számok:")
	for i in range(1, 101, 2):
		print(i, end=" ")
	print("\nC) 3-mal osztható számok:")
	for i in range(3, 101, 3):
		print(i, end=" ")
	print("\nD) 3-mal osztva 2 maradék:")
	for i in range(1, 101):
		if i % 3 == 2:
			print(i, end=" ")
	print("\nE) Páros számok négyzete 20-ig:")
	for i in range(2, 21, 2):
		print(i**2, end=" ")
	print("\nF) Négyzetszámok 100-ig:")
	for i in range(1, 11):
		print(i**2, end=" ")
	print("\nG) Első 15 négyzetszám:")
	for i in range(1, 16):
		print(i**2, end=" ")
	print("\nH) Számok négyzetgyöke 100-ig:")
	import math
	for i in range(1, 101):
		print(f"{i}: {math.sqrt(i):.2f}", end="; ")
	print()

# 8. feladat
def osszegzesek():
	print("8. feladat: Összegzések")
	print("A) Páros számok összege 100-ig:", sum(i for i in range(2, 101, 2)))
	print("B) Páratlan számok összege 100-ig:", sum(i for i in range(1, 101, 2)))
	print("C) 3-mal osztható számok összege 100-ig:", sum(i for i in range(3, 101, 3)))
	print("D) 3-mal osztva 2 maradék összege:", sum(i for i in range(1, 101) if i % 3 == 2))
	print("E) Páros számok négyzetének összege 20-ig:", sum(i**2 for i in range(2, 21, 2)))
	print("F) Négyzetszámok összege 100-ig:", sum(i**2 for i in range(1, 11)))
	print("G) Első 15 négyzetszám összege:", sum(i**2 for i in range(1, 16)))
	import math
	print("H) Számok négyzetgyökeinek összege 100-ig:", sum(math.sqrt(i) for i in range(1, 101)))

# 9. feladat
def primszamok():
	print("9. feladat: Prímszámok")
	def is_prime(n):
		if n < 2:
			return False
		for i in range(2, int(n**0.5)+1):
			if n % i == 0:
				return False
		return True
	# A) Bekér egy számot, eldönti, hogy prím-e
	n = int(input("Adj meg egy számot: "))
	print("Prím" if is_prime(n) else "Nem prím")
	# B) 2..100-ig prímek
	print("Prímek 2-től 100-ig:")
	for i in range(2, 101):
		if is_prime(i):
			print(i, end=" ")
	print()
	# C) Első N db prím
	N = int(input("Hány prím számot írjak ki? "))
	count = 0
	i = 2
	while count < N:
		if is_prime(i):
			print(i, end=" ")
			count += 1
		i += 1
	print()
	# D) Eratoszthenész szita 1..200
	print("Prímek 1-től 200-ig (szita):")
	limit = 200
	szita = [True] * (limit+1)
	szita[0] = szita[1] = False
	for i in range(2, int(limit**0.5)+1):
		if szita[i]:
			for j in range(i*i, limit+1, i):
				szita[j] = False
	for i in range(2, limit+1):
		if szita[i]:
			print(i, end=" ")
	print()

# 10. feladat
def veletlenek():
	print("10. feladat: Véletlenek, kockadobás, TOTO")
	import random
	print("A) Egy véletlen szám 1-100 között:", random.randint(1, 100))
	print("B) Tíz kockadobás:")
	dobasok = [random.randint(1, 6) for _ in range(10)]
	print(dobasok)
	print("C) Tíz kockadobás összege:", sum(dobasok))
	print("D) 6000 dobásból hányszor volt hatos?")
	dobasok6000 = [random.randint(1, 6) for _ in range(6000)]
	print(dobasok6000.count(6))
	print("E) 6000 dobásból hányszor volt egyes, kettes, ...?")
	for i in range(1, 7):
		print(f"{i}: {dobasok6000.count(i)}")
	print("F) 6000 dobás átlag:", sum(dobasok6000)/6000)
	print("G) Egy TOTO szelvény tippjei:")
	toto = [random.choice(['1', '2', 'X']) for _ in range(14)]
	print(toto)
# 4. feladat
# A) Négyzet vagy téglalap eldöntése
def pozitiv_bekeres(szoveg):
	szam = float(input(szoveg))
	while szam < 0:
		print("Csak pozitív számot adj meg!")
		szam = float(input(szoveg))
	return szam

A = pozitiv_bekeres("Add meg az A oldalt: ")
B = pozitiv_bekeres("Add meg a B oldalt: ")
if A == B:
	print("Négyzet")
else:
	print("Téglalap")

# B) Téglalap területe
terulet = A * B
print(f"Terület: {terulet}")

# C) Téglalap terület és kerület
kerulet = 2 * (A + B)
print(f"Kerület: {kerulet}")

# D-E) Négyzet/téglalap, terület, kerület, csak pozitív oldal
# (már megvalósítva fentebb)

# F) Kör terület és kerület, sugár nem lehet negatív
import math
def pozitiv_sugar():
	r = float(input("Add meg a kör sugarát: "))
	while r < 0:
		print("Csak pozitív sugarat adj meg!")
		r = float(input("Add meg a kör sugarát: "))
	return r

r = pozitiv_sugar()
kor_terulet = math.pi * r ** 2
kor_kerulet = 2 * math.pi * r
print(f"Kör területe: {kor_terulet}, kerülete: {kor_kerulet}")

# G) Háromszög szerkeszthetőség és típus
def haromszog_tipus():
	a = float(input("a oldal: "))
	b = float(input("b oldal: "))
	c = float(input("c oldal: "))
	if a + b > c and a + c > b and b + c > a:
		if a == b == c:
			print("Szabályos háromszög")
		elif a == b or b == c or a == c:
			print("Egyenlő szárú háromszög")
		else:
			print("Általános háromszög")
	else:
		print("Nem szerkeszthető háromszög!")

haromszog_tipus()
# 3. feladat
# A) Celsius fokot Kelvinbe
celsius = float(input("Add meg a hőmérsékletet Celsiusban: "))
kelvin = celsius + 273.15
print(f"Kelvin: {kelvin}")

# B) Méter átváltása cm-be, mm-be
meter = float(input("Add meg a távolságot méterben: "))
cm = meter * 100
mm = meter * 1000
print(f"Centiméter: {cm}, Milliméter: {mm}")

# C) Óra:Perc:mp átváltása mp-be
ora = int(input("Óra: "))
perc = int(input("Perc: "))
mp = int(input("Másodperc: "))
osszes_mp = ora * 3600 + perc * 60 + mp
print(f"Összesen másodpercben: {osszes_mp}")

# D) mp átváltása Óra:Perc:mp-be
mp2 = int(input("Add meg az időt másodpercben: "))
ora2 = mp2 // 3600
perc2 = (mp2 % 3600) // 60
mp_maradek = mp2 % 60
print(f"{ora2}:{perc2}:{mp_maradek}")
# 2. feladat
# Eldönti a beolvasott vízhőmérséklet alapján, hogy milyen halmazállapotú
vizho = float(input("Add meg a víz hőmérsékletét (°C): "))
if vizho <= 0:
	print("Szilárd (jég)")
elif vizho < 100:
	print("Folyékony")
else:
	print("Légnemű (gőz)")
# 1. feladat
# A) Eldönti egy beolvasott számról, hogy pozitív vagy negatív
szam = int(input("Adj meg egy számot: "))
if szam > 0:
	print("A szám pozitív.")
elif szam < 0:
	print("A szám negatív.")
else:
	print("A szám nulla.")

# B) A beolvasott két szám közül a nagyobbat írja ki
szam1 = int(input("Adj meg az első számot: "))
szam2 = int(input("Adj meg a második számot: "))
if szam1 > szam2:
	print(f"A nagyobb szám: {szam1}")
elif szam2 > szam1:
	print(f"A nagyobb szám: {szam2}")
else:
	print("A két szám egyenlő.")

# C) A beolvasott két szám közül a kisebbet írja ki
if szam1 < szam2:
	print(f"A kisebb szám: {szam1}")
elif szam2 < szam1:
	print(f"A kisebb szám: {szam2}")
else:
	print("A két szám egyenlő.")
print('hello world')
