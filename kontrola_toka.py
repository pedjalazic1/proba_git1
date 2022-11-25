import random

#strukture za kontrolu toka je set instrukcija koje omogucavaju da program donosi neke odluke 

# #primer 
# x = 10  
# # print(x > 0)
# # print("x je pozitivan broj.")

# # IF struktura toka  
# # IF(expression): block
# # IF expression : block 

# #mora biti boolean  TRUE ili FALSE

# #primer 2 uvlaka koda 

# if x > 0: 
#     print("broj x je pozitivan")

# print("izvrsava se u savkom slucaju")

# # Ugnjezdeni 

# vozilo_u_pokretu = True
# brzina = 60
# if vozilo_u_pokretu == True: #uvek idu 2 tacke 
#     print("vozilo se krece...") #mora se razmaknuti sa TAB-om
# # dve tacke umesto == imaju isto znacenje ako smo vec zadali true ili false koju smo napisali u njenoj vrednosti


#     print("vozilo se krece...")
#     print("proverite i brzinu...")
#     if brzina > 50:
#         print("prekoracena brzina")
#     print("ovo izvrsavam kolika god da je brzina")
#     if brzina <=50:
#         print("brzina je OK.")
# if vozilo_u_pokretu = False:
#     print("vozilo se ne krece")
proizvod = "duks"
cena = 3000

# komanda = int(input("unesite komandu:  "))


# if komanda == 1:
#     print("prikazati proizvode") 
#     print("proizvod:",proizvod,"cena",cena)
# if komanda == 2:
#     print("kupovina")
#     stanje = int(input("unesite stanje na racunu:  "))
#     if stanje >= cena:
#         print("uspesna kupovina")
#     if stanje < cena:
#         print("neuspesna kupovina")

# if komanda == 3:
#         print("izlaz")

# ELSE STRUKTURA ili rezervna varijanta umesto IF
#primer 

broj = 5

if broj > 0:
    print("broj je veci od 0.")
    
else:
    print("broj je 0 ili manji od 0.")

marija = False
ksenija = True
olga = False
devojka_na_dejtu = ""

if marija:
    devojka_na_dejtu = "marija"
elif olga:
    devojka_na_dejtu = "olga"
elif ksenija:
    devojka_na_dejtu = "ksenija"
else:
    devojka_na_dejtu = "sofija"

print("izlazis sa:",devojka_na_dejtu)


# ELIF IZJAVA
# elif se moze posmatrati kao ELSE sa dodatnim uslovom
#ako ne rade if i elif ozvrsava se else tj rezerva 


#drugi deo casa


automobil_polovan = False # nov
godiste = 2021
boja = "crna" 


if (automobil_polovan == True or godiste > 2017) and boja == "crna":
    print("kupujem")

# skracivanje 
# NOT pretvara False u True
if not automobil_polovan == True:
    print("automobil je polovan.")

prisutan = False #nije prisutan7
prisutan = True #jeste prosutan

if prisutan: 
    print("na casu je")
if not prisutan:
    print("nije na casu")

smer = "python"

if  prisutan and smer == "python":
    print("polaznik je bio na casu")

#RANDOM BROJ 

# trenutni_rezultat = random.randint(1,100)
# novi_rezultat = int(input("unesite novi broj( od 1 do 100): "))

# if novi_rezultat > 100 or novi_rezultat < 1:
#     print("proverite broj,dozvoljeno od 1 do 100")

# else:
#     if trenutni_rezultat < novi_rezultat:
#         print("pobedili ste")
#     elif trenutni_rezultat == novi_rezultat:
#         print("indenticne vrednosti")
#     else:
#         print("izubili ste")


# TERNARNI OPERATOR je specijalan zapis IF ELSE izraza u kome oba slucaja reyultiraju konteksteualno istom vrednosu

#primer

# pol = "m"
# poruka = ""

# if pol == "m":
#     poruka = "hey mister!"
# else:
#     poruka = "hey miss!"

# # izmena ovog gore tj skracenica 

# poruka = "hey mister!" if pol == "m" else "hey miss!"
# print(poruka)


# popularan_proizvod = "ajvar"
# jesen = True

# if jesen == True:
#     print("ajvar")

# else: 
#     print(popularan_proizvod)



# PETLJEE MNOGO BITNOOOOOOOOO 





        
        

        



































        


 













