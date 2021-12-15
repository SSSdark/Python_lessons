# 9-dars
# 15.12.2021
#Shohrux Shirinboyev


#friends = ["Ahror", "Dilmurod", "Mehroj", "Sobir", "Mizik"]
#for n in friends:
#    print("Salom", n)
#a = len(friends)
#print ("Kod", a, "marta takrorlandi")

#ruyxat = list(range(11, 100, 2))
#for n in ruyxat:
#    print(n**3)

#kinolar = []
#print ("5 ta sevimli kinoyingizni kiriting")
#for k in range(5):
#    kinolar.append(input(f"{k + 1} - kino:"))


soni = int(input("Siz bugun nechi kishi bilan suhbat qurdingiz?\n >>>"))
odamlar = []
for odam in range(soni):
    odamlar.append(input(f"{odam + 1} - suhbat qilgan odamingiz kim edi:"))
print(odamlar)
