# 15-dars
# 30.01.2022
# Shokhrukh Shirinboev


pil = {'if' : 'agar', 'elsa' : 'aks holda', 'integer' : 'butun son', 'float' : 'haqiqiy son', 'string' : 'belgili ifoda', 'true' : 'rost ifoda', 'list' : "ro'yxat", 'false' : "yolg'on"}
#print(pil.items())

#for kalit, qiymat in pil.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat} \n")


#for k, q in sorted(pil.items()):
#    print(f"{k.title()} - {q}")

dvp = {'USA' : 'Washington', "Qirg'iziston" : "Bishkek",
        "Qozog'iston" : "Nursulton", "Italiya" : "Rim",
        "Tojikiston" : "Dushanbe", "Rossiya" : "Moskva",
        "Ispaniya" :"Madrid", "Fransiya" : "Parij",
        "UK" : "London", "Germaniya" : "Berlin"}

#print(sorted(dvp.keys()))
#print(sorted(dvp.values()))

#for davlat in sorted(dvp):
#    print(davlat.upper())

#for poytaxt in sorted(dvp.values()):
#    print(poytaxt.title())

#name = input(str("Qaysi davlatning poytaxtini bilishni istaysiz? \>>>"))
#capital = dvp.get(name)
#if capital == None:
#    print("Kechirasiz bizda bu haqida ma'lumot yo'q")
#else:
#    print(f"{name} davlatining poytaxxti {capital}")


menu = {"osh" : "25000 so'm", "manti" : "4000 so'm", 
        "somsa" : "6000 so'm", "bishteks" : "18000 so'm",
        "sho'rva" : "15000 so'm", "lag'mon" : "15000 so'm",
        "kabob" : "14000 so'm", "salat" : "1000 so'm",
        "suzma" : "500 so'm", "choy" : "tekin"
        }

print ("3 ta taom buyurtma bering")
#taom_1 = input(str("1-taom ga nima buyurtma berasiz\>>>"))
#taom_2 = input(str("2-taom ga nima buyurtma berasiz\>>>"))
#taom_3 = input(str("3-taom ga nima buyurtma berasiz\>>>"))

buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]}")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")