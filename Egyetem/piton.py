# 21. feladat
def ketdimenzios_tomb_muveletek():
	print("21. feladat: Kétdimenziós tömb műveletek")
	sor = int(input("Sorok száma: "))
	oszlop = int(input("Oszlopok száma: "))
	tomb = []
	for i in range(sor):
		sor_lista = []
		for j in range(oszlop):
			sor_lista.append(float(input(f"Elem [{i+1},{j+1}]: ")))
		tomb.append(sor_lista)
	print("A) Táblázat:")
	for sor_lista in tomb:
		print("\t".join(str(x) for x in sor_lista))
	min_elem = min(min(sor_lista) for sor_lista in tomb)
	print("B) Legkisebb elem:", min_elem)
	osszeg = sum(sum(sor_lista) for sor_lista in tomb)
	print("C) Összeg:", osszeg)
	print("D) Soronként összeg, átlag:")
	for sor_lista in tomb:
		print("Összeg:", sum(sor_lista), "Átlag:", sum(sor_lista)/len(sor_lista))
	print("E) Soronként legnagyobb, legkisebb:")
	for sor_lista in tomb:
		print("Max:", max(sor_lista), "Min:", min(sor_lista))
	print("F) Soronként összeg, átlag, min, max külön tömbbe:")
	osszeg_tomb = [sum(sor_lista) for sor_lista in tomb]
	atlag_tomb = [sum(sor_lista)/len(sor_lista) for sor_lista in tomb]
	min_tomb = [min(sor_lista) for sor_lista in tomb]
	max_tomb = [max(sor_lista) for sor_lista in tomb]
	print("Összeg tömb:", osszeg_tomb)
	print("Átlag tömb:", atlag_tomb)
	print("Min tömb:", min_tomb)
	print("Max tömb:", max_tomb)
	print("G) Rendezett sorok:")
	for sor_lista in tomb:
		print(sorted(sor_lista))

# 22. feladat
def uszoverseny_pontozas():
	print("22. feladat: Úszóverseny pontozás")
	N = int(input("Versenyzők száma: "))
	M = int(input("Bírók száma: "))
	pontok = []
	for i in range(N):
		pontok.append([int(input(f"Versenyző {i+1}, bíró {j+1} pontja: ")) for j in range(M)])
	osszpontszamok = [sum(sor) for sor in pontok]
	maxpont = max(osszpontszamok)
	minpont = min(osszpontszamok)
	print("A) Győztes(ek):", [i+1 for i, p in enumerate(osszpontszamok) if p == maxpont])
	print("B) Legtöbb pontot adó bíró:", max(range(M), key=lambda j: sum(p[j] for p in pontok))+1)
	print("C) Győztesnek legtöbb/legkevesebb pontot adó bíró:")
	gyoztes_idx = osszpontszamok.index(maxpont)
	print("Max:", pontok[gyoztes_idx].index(max(pontok[gyoztes_idx]))+1, "Min:", pontok[gyoztes_idx].index(min(pontok[gyoztes_idx]))+1)
	print("D) Első három helyezett összpontszáma:", sorted(osszpontszamok, reverse=True)[:3])
	print("E) Legnagyobb pontot először adó bíró:")
	for j in range(M):
		for i in range(N):
			if pontok[i][j] == 10:
				print(f"Bíró {j+1} versenyző {i+1}")
				break
	print("F) Vesztes:", osszpontszamok.index(minpont)+1)
	print("G) Különbség győztes és vesztes között:", maxpont-minpont)
	print("H) Átlagpontszám versenyzőnként:", [sum(sor)/M for sor in pontok])
	print("I) Átlagpontszám összesen:", sum(sum(sor) for sor in pontok)/(N*M))
	print("J) Kiadott összpontszám:", sum(sum(sor) for sor in pontok))
	print("K) Versenyzőnként összpontszám:", osszpontszamok)
	print("L) Holtversenyek:")
	from collections import Counter
	c = Counter(osszpontszamok)
	for pont, db in c.items():
		if db > 1:
			print(f"{db} versenyző {pont} ponttal")

# 23. feladat
def sakktabla_feladatok():
	print("23. feladat: Sakktábla feladatok (egyszerűsített)")
	print("A) 8-8 gyalog véletlenszerűen elhelyezve, kiütések száma nem implementált.")
	print("B) 2-2 bástya ütik-e egymást? (egyszerűsített)")
	bastyak = [(int(input("Bástya 1 sor: ")), int(input("Bástya 1 oszlop: "))),
			   (int(input("Bástya 2 sor: ")), int(input("Bástya 2 oszlop: ")))]
	if bastyak[0][0] == bastyak[1][0] or bastyak[0][1] == bastyak[1][1]:
		print("Ütik egymást!")
	else:
		print("Nem ütik egymást.")
	print("C) Bástya és gyalog ütés vizsgálata nem implementált.")

# 24. feladat
def dolgozat_osztalyozas():
	print("24. feladat: Dolgozat osztályozás")
	pont = int(input("Pontszám: "))
	if pont >= 90:
		print("Jeles (5)")
	elif pont >= 75:
		print("Jó (4)")
	elif pont >= 60:
		print("Közepes (3)")
	elif pont >= 40:
		print("Elégséges (2)")
	else:
		print("Elégtelen (1)")

# 25. feladat
def siknegyed():
	print("25. feladat: Melyik síknegyedben van a pont?")
	x = float(input("x koordináta: "))
	y = float(input("y koordináta: "))
	if x > 0 and y > 0:
		print("I. síknegyed")
	elif x < 0 and y > 0:
		print("II. síknegyed")
	elif x < 0 and y < 0:
		print("III. síknegyed")
	elif x > 0 and y < 0:
		print("IV. síknegyed")
	else:
		print("A pont valamelyik tengelyen vagy az origóban van.")
# 16. feladat
def rendezett_e_tomb():
	print("16. feladat: Rendezett-e a tömb?")
	N = int(input("Hány elemű legyen a tömb? "))
	tomb = [float(input(f"{i+1}. elem: ")) for i in range(N)]
	nov = all(tomb[i] <= tomb[i+1] for i in range(N-1))
	csokk = all(tomb[i] >= tomb[i+1] for i in range(N-1))
	print("Növekvő rendezett:" if nov else "Nem növekvő rendezett.")
	print("Csökkenő rendezett:" if csokk else "Nem csökkenő rendezett.")

# 17. feladat
def szetvalogatas_10_alapjan():
	print("17. feladat: Tömb szétválogatása 10 alapján")
	N = int(input("Hány elemű legyen a tömb? "))
	tomb = [float(input(f"{i+1}. elem: ")) for i in range(N)]
	nagyobb = [x for x in tomb if x > 10]
	kisebb = [x for x in tomb if x < 10]
	print("10-nél nagyobbak:", nagyobb)
	print("10-nél kisebbek:", kisebb)

# 18. feladat
def szetvalogatas_tobb_tombbe():
	print("18. feladat: Tömb szétválogatása több tömbbe")
	N = int(input("Hány elemű legyen a tömb? "))
	tomb = [float(input(f"{i+1}. elem: ")) for i in range(N)]
	t0_10 = [x for x in tomb if 0 <= x <= 10]
	t11_20 = [x for x in tomb if 11 <= x <= 20]
	tobbi = [x for x in tomb if x < 0 or x > 20]
	print("0-10:", t0_10)
	print("11-20:", t11_20)
	print("Többi:", tobbi)

# 19. feladat
def rendez_fuz():
	print("19. feladat: Tömbök rendezése és összefűzése")
	t0_10 = sorted([float(input(f"0-10 szám: ")) for _ in range(3)])
	t11_20 = sorted([float(input(f"11-20 szám: ")) for _ in range(3)])
	tobbi = sorted([float(input(f"Többi szám: ")) for _ in range(3)])
	osszefuzve = t0_10 + t11_20 + tobbi
	print("Összefűzött tömb:", osszefuzve)

# 20. feladat
def osszegzes_elottelevovel():
	print("20. feladat: Minden elemhez hozzáadjuk az előtte lévőt")
	N = int(input("Hány elemű legyen a tömb? "))
	tomb = [float(input(f"{i+1}. elem: ")) for i in range(N)]
	uj_tomb = []
	for i in range(N):
		if i == 0:
			uj_tomb.append(tomb[i])
		else:
			uj_tomb.append(tomb[i] + tomb[i-1])
	print("Új tömb:", uj_tomb)
# 11. feladat
def szamkitalalo():
	import random
	print("11. feladat: Számkitaláló játék")
	gondolt = random.randint(1, 100)
	lepes = 0
	while True:
		tipp = int(input("Tippelj (1-100): "))
		lepes += 1
		if tipp < gondolt:
			print("Nagyobb számra gondoltam.")
		elif tipp > gondolt:
			print("Kisebb számra gondoltam.")
		else:
			print(f"Eltaláltad {lepes} lépésből!")
			break

# 12. feladat
def tomb_muveletek():
	print("12. feladat: Tömb műveletek")
	tomb = []
	for i in range(10):
		szam = float(input(f"{i+1}. szám: "))
		tomb.append(szam)
	print("B) Tömb tartalma:", tomb)
	print("C) Csak pozitív számokat kér be:")
	tomb_poz = []
	while len(tomb_poz) < 10:
		szam = float(input(f"Pozitív szám ({len(tomb_poz)+1}/10): "))
		if szam > 0:
			tomb_poz.append(szam)
	print("D) Pozitív elemek:", [x for x in tomb if x > 0])
	print("E) Negatív elemek száma:", sum(1 for x in tomb if x < 0))
	print("F) Tömb összege:", sum(tomb))
	print("G) Tömb átlaga:", sum(tomb)/len(tomb))
	szorzat = 1
	for x in tomb:
		szorzat *= x
	print("H) Tömb szorzata:", szorzat)
	print("I) Összeg, átlag, szorzat:", sum(tomb), sum(tomb)/len(tomb), szorzat)

# 13. feladat
def bekert_szamok_muveletek():
	print("13. feladat: Bekért számok műveletei (tömb nélkül)")
	osszeg = 0
	szorzat = 1
	szamok = []
	for i in range(10):
		szam = float(input(f"{i+1}. szám: "))
		osszeg += szam
		szorzat *= szam
		szamok.append(szam)
	print("A) Összeg:", osszeg)
	print("B) Átlag:", osszeg/10)
	print("C) Szorzat:", szorzat)
	print("D) Összeg, átlag, szorzat:", osszeg, osszeg/10, szorzat)

# 14. feladat
def tomb_elem_vizsgalatok():
	print("14. feladat: Tömb elem vizsgálatok")
	N = int(input("Hány elemű legyen a tömb? "))
	tomb = [float(input(f"{i+1}. elem: ")) for i in range(N)]
	print("A) Van-e pozitív elem:", any(x > 0 for x in tomb))
	print("B) Van-e negatív elem:", any(x < 0 for x in tomb))
	print("C) Szerepel-e 10-es szám:", 10 in tomb)
	keresett = float(input("D) Melyik számot keresed? "))
	print("Szerepel-e:", keresett in tomb)
	print("E) Első pozitív elem:", next((x for x in tomb if x > 0), None))
	print("F) Pozitív elemek:", [x for x in tomb if x > 0])
	print("G) Pozitív elemek összege:", sum(x for x in tomb if x > 0))
	print("H) Negatív elemek:", [x for x in tomb if x < 0])
	print("I) Negatív elemek száma:", sum(1 for x in tomb if x < 0))
	print("J) Negatív és pozitív elemek száma:", sum(1 for x in tomb if x < 0), sum(1 for x in tomb if x > 0))
	print("K) 10-es szám indexe:", tomb.index(10)+1 if 10 in tomb else 0)
	print("L) Legkisebb elem:", min(tomb), "Index:", tomb.index(min(tomb))+1)
	print("M) Legnagyobb elem:", max(tomb), "Index:", tomb.index(max(tomb))+1)
	print("N) Legnagyobb és legkisebb elem:", max(tomb), min(tomb))
	print("O) Legnagyobb elem előfordulása:", tomb.count(max(tomb)))
	tomb_rendezett = sorted(tomb)
	print("P) Második legnagyobb/kisebb:", tomb_rendezett[-2], tomb_rendezett[1])
	print("Q) Növekvő sorrend:", tomb_rendezett)
	print("R) Csökkenő sorrend:", sorted(tomb, reverse=True))

# 15. feladat
def minimum_kivalasztas_rendezes():
	print("15. feladat: Minimum kiválasztásos rendezés")
	N = int(input("Hány elemű legyen a tömb? "))
	tomb = [float(input(f"{i+1}. elem: ")) for i in range(N)]
	for i in range(N-1):
		min_idx = i
		for j in range(i+1, N):
			if tomb[j] < tomb[min_idx]:
				min_idx = j
		tomb[i], tomb[min_idx] = tomb[min_idx], tomb[i]
	print("Rendezett tömb:", tomb)
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
