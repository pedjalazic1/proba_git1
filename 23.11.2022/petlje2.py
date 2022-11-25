# na proslom casu smo imali for i while petlje


# for x in range (1,7):
#     for y in range(5):
#         print("#",end="")
#     print("novi red")

#####novi red
#####novi red
#####novi red
#####novi red
#####novi red
#####novi red



# for x in range (10):
#     for y in range (10):
#         if y > x :
#          print("#",end="")
#         else:
#             print("",end="")
#     print()



# # WHILE 


# automobil = 0
# cilj = 100

# brzina = 10

# while automobil<cilj:
#     print("voznja je u toku.")
#     automobil += brzina

# else: 
#     print("stigli ste")

# voznja je u toku.
# voznja je u toku.
# voznja je u toku.
# voznja je u toku.
# voznja je u toku.
# voznja je u toku.
# voznja je u toku.
# voznja je u toku.
# voznja je u toku.
#stigli ste



# SEKVENCE je uredjena kolekcija podataka unutar koje se vrednosti mogu ponavljati


# PRIMER

#prvi clan(index 0)...drugi (1).....treci (2).....cetvrti (3)

osoba = ["Sofija",20,"boja kose plava",True]
print(osoba)

print(osoba[0])
print("godine",osoba[1])


#['Sofija', 20, 'boja kose plava', True]
#Sofija
#godine 20


automobili = ["opel","honda","toyota"]
print(automobili[1])
#honda
#            0           1          2          3
vreme = ["oblacno","maglovito","kisovito","lepo vreme"]
print(vreme[0])
#oblacno

#TIPOVI SEKVENCI

# OPSEG (RANGE)
# STRING (STRING)
# LISTA (LIST)
# TUPLE (TUPLE)
# NIZ BAJTOVA (BYTE ARRAY)
# SEKVENCA BAJTOVA (BYTE SEQUENCE)

#1 RANGE/OPSEG

for x in range (5,10,2): # mozemop i dodati (5,10,-1) racuna od 10 u minus
    print(x)
# prvi rezultat 1.2.3.4.5.6.7.8.9
# drugi 5...6...7...8...9.
# treci 5...7...9.

#       01234567891011
kurs = "python course" # sekvenca racuna i razmak (SPACE)
print(kurs[0])
print(kurs[1])
print(kurs[2])
print(kurs[3])


for x in range(13):
    print(kurs[x]) # ispisuje se u pdajucem nizu "python course"



for x in range (13):
    print("na poziciji:",x,kurs[x])

 #na poziciji: 0 p
# na poziciji: 1 y
# na poziciji: 2 t
# na poziciji: 3 h
# na poziciji: 4 o
# na poziciji: 5 n
# na poziciji: 6
# na poziciji: 7 c
# na poziciji: 8 o
# na poziciji: 9 u
# na poziciji: 10 r
# na poziciji: 11 s
# na poziciji: 12 e

# duzina = len(kurs)

# for x in range(len(kurs)):
#      print("na pozociji:",x,kurs(x))


ustanova = "IT ACADEMY"

for indeks in range (len(ustanova)):
    print(ustanova[indeks])


primer = "zadatak1"

for primer in range(8):
    print("zadatak1"[primer]) # moj primer

primer = "zadatak1"
for x in range (len(primer)):
    print(primer[x],end= "") # ispravan nikolin primer


# PRIMPER SA WHILE PETLJOM 

broj_karatktera = len(primer)
indeks = 0

while indeks<broj_karatktera:
    print(primer[indeks]) #ovako nece raditi ide u beskonacan kod 
    indeks += 1  # dodajemo += 1 da bi se pravilno ispisao


# OPERACIJE NAD STRING-om  

# OPERACIJA STRINGA  name = "predrag" name_valid = name,upper() print (name_valid)



# korisnicko_ime = "admin"
# uneto_korisnicko_ime = input("Unesi korisnicko ime:")

# if korisnicko_ime == uneto_korisnicko_ime.lower(): #komanda lower prepoznaje velika i mala slova (admin)==(AdMin)
#     print("dobrodosli")
# else:
#     print("pogresni podaci")



# racunar = "laptop"
# model = "PH"
# racunar[1]= "c"
# racunar + model
# racunar = "desktop"


# DRUGI DEO CASA "LISTE" 
# liste su sekvence podataka istog ili razlicitih tipova podataka

osoba = ["Sofija",25,"plava",False]

for x in range(len(osoba)):
    print(osoba[x])

#Sofija
#25
#plava
#False

for osobina in osoba :
    print(osobina)
#Sofija
#25
#plava
#False



voce_i_povrce = ["jabuka","banana","kruska","kajsija"]

#1 
for stavka in voce_i_povrce:
    print(stavka)
#jabuka
#banana
#kruska
#kajsija

#2
for i in range(len(voce_i_povrce)):
    print(voce_i_povrce[i])

#jabuka
# banana
# kruska
# kajsija
vrednost=0
for i in range(len(voce_i_povrce)):
    print("ma indeksu:",i,"nalazi se",voce_i_povrce[i])

#ma indeksu: 0 nalazi se jabuka
# ma indeksu: 1 nalazi se banana
# ma indeksu: 2 nalazi se kruska
# ma indeksu: 3 nalazi se kajsija


for indeks,vrednost in enumerate(voce_i_povrce):
    print("indeks",indeks,"stavka",vrednost)
#indeks 0 stavka jabuka
# indeks 1 stavka banana
# indeks 2 stavka kruska
# indeks 3 stavka kajsija


#                0       1      2    3    indeks stavke vrednosti i njene pozicije 
automobili=["citroen","audi","bmw","kec","yugo","opel"]

for pozicija,auto in enumerate(automobili):
    print("pozicija:",pozicija,"auto:",auto)

# print(automobili[2]) dobijamo bmw


# pozicija: 0 auto: citroen
# pozicija: 1 auto: audi
# pozicija: 2 auto: bmw
# pozicija: 3 auto: opel



for pozicija,auto in enumerate(automobili):
    if len(auto) == 3:
        print(auto)
#bmw

automobili.append("opel")

print(automobili)

#['citroen', 'audi', 'bmw', 'opel', 'opel', 'opel', 'opel']



automobili.append("mercedes")
automobili[2]= "opel"
print(automobili)
automobili[3] = "audi"


del automobili[3]
print(automobili)

#['citroen', 'audi', 'opel', 'yugo', 'opel', 'opel', 'mercedes'] izbacio je poziciju 3




# SLICE (slic/ovi) nova sekvenca koju pravimo na osnovu postojece sekvence

automobili=["citroen","audi","bmw","kec","yugo","opel","skoda"]

automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i]) # primer sa casa tezi nacin

print(automobili_akcija)


# ['audi', 'bmw', 'kec']


automobili_akcija = automobili [1:4] # nikolin laksi primer 
print(automobili_akcija)

# ['audi', 'bmw', 'kec']

brojevi= [1,3,5,6,8,10,12,24,45]
parni=[]
neparni=[]

for broj in brojevi:
    if broj %2 == 0:
        parni.append(broj)

print(parni,neparni)

#[6, 8, 10, 12, 24] 

brojevi= [1,3,5,6,8,10,12,24,45]
parni=[]
neparni=[]

for broj in brojevi:
    parni.append(x) if x % 2 == 0 else neparni.append(x) # nikolin primer

print(parni,neparni)
    






















