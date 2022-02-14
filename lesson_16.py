#lesson 16
#Shohrux Shirinboev
#08.02.2022

#adiblar = {}
#adiblar[0] = {'ism' : 'Abu', 'familiya' : 'Abdulloh', 'tyil' : 810, 'tjoy' : 'Buxoro', 'yosh' : 60, 'asarlar' : ["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]}
#adiblar[1] = {'ism' : 'Abdulla', 'familiya' : 'Qodiriy', 'tyil' : 1894, 'tjoy' : 'Toshkent', 'yosh' : 44, 'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']}
#adiblar[2] = {'ism' : 'Erkin', 'familiya' : 'Vohidovv', 'tyil' : 1936, 'tjoy' : "Farg'ona", 'yosh' : 80, 'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]}
#adiblar[3] = {'ism' : 'Alisher', 'familiya' : 'Navoiy', 'tyil' : 1441, 'tjoy' : 'Hirot', 'yosh' : 60, 'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']} 

#for info, adib in adiblar.items():
#    print(f"{adib['ism']} {adib['familiya']}, "
#    f"{adib['tyil']}-yilda, {adib['tjoy']}da tug'ilgan, "
#    f"{adib['yosh']} yil umr ko'rgan"
#    )


#for info, adib in adiblar.items():
#    ism = adib['ism']
#    asar = adib['asarlar']
#    print(f"\n {ism} ning mashhur asarlari:")
#    for n in asar:
#        print(n)


#2-usul
#shaxslar = [adiblar[0], adiblar[1], adiblar[2], adiblar[3]]
#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    asar = shaxs['asarlar']
#    print(f"\n {ism} ning mashhur asarlari:")
#    for n in asar:
#        print(n)


#ali = ['terminator' , 'sevginator' , 'titanic']
#vali = ['tenet', 'inception', 'virus']
#hasan = ['abdullajon', 'bomba' , 'shaytanat']
#husan = ['john wick', "Adolat kurashchisi", "g'azab"]

#kinolar = {'Ali' : ali, 'Vali' : vali, 'Hasan' : hasan, 'Husan' : husan}

#for ism, kino in kinolar.items():
#    print(f'{ism} ning sevimli kinolari:')
#    for n in kino:
#        print(n.capitalize())


davlatlar = {"O'zbekiston" : {'poytaxti' : 'Toshkent', "hududi" : "448978 km.kv", 'aholisi': 37000000, 'pul birligi' : "so'm"}
, "Rossiya" : {'poytaxti' : 'Moskva', "hududi" : "17098246 km.kv", 'aholisi': 144000000, 'pul birligi' : "rubl"}
, "AQSh" : {'poytaxti' : 'Vashington', "hududi" : "9631418 km.kv", 'aholisi': 327000000, 'pul birligi' : "dollar"}
, "Malayziya" : {'poytaxti' : 'Kuala-Limpur', "hududi" : "329750 km.kv", 'aholisi': 25000000, 'pul birligi' : "rinngit"}
}

#for davlat, info in davlatlar.items():
#    print(f"{davlat} haqida ma'lumotlar:")
#    for n, m in info.items():
#        print(f"{n}:{m}")

        
davlat = input('Davlat nomini kiriting: ')
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxti'].title()}"
          f"\nHududi: {info['hududi']} kv.km"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
        

