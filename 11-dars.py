# 11-dars
# 17.12.2021
# Shohrux Shirinboyev

#son = int(input("Istalgan butun sonni kiriting\n>>>"))
#if (son % 2) == 0:
#    print("siz kiritgan son", son, "juft son")
#else:
#    print("siz kiritgan son", son, "toq son")


#yosh  = int(input("Yoshingizni kiriting\n>>>"))
#if yosh < 4 or yosh > 60:
#    print("Bilet narxi: bepul")
#elif yosh < 18:
#    print("Bilet narxi: 10000 sum")
#else:
#    print("bilet narxi: 20000 sum")


#son1 = float(input('1-sonni kiriting\n>>>'))
#son2 = float(input('2-sonni kiriting\n>>>'))
#if son1 > son2:
#    print(son1,">",son2)
#elif son1 == son2:
#    print(son1,"=",son2 )
#else:
#    print(son1,"<",son2)


#mahsulotlar = ['non', 'tuxum', 'kartoshka', 'piyoz', 'pomidor', 'tomat', 'un', 'shakar', 'sabzi', 'banan']
#savat = []
#for n in range(5):
#    print(savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ")))
#
#for product in savat:
#    if product in mahsulotlar:
#        print(product ,"do'konimizda bor")
#    else:
#        print(product ,"do'konimizda yo'q")
#
#mavjud_emas = []
#bor_mahsulotlar = []
#for product in savat:
#    if product in mahsulotlar:
#        bor_mahsulotlar.append(product)
#    else:
#        mavjud_emas.append(product)

#a = len(mavjud_emas)
#if a != 0:
#    print("bizning do'konda quyidagi mahsulotlar mavjud emas")
#    print(mavjud_emas)
#else:
#    print("Bizning do'konda siz izlagan hamma mahsulotlar mavjud")

#foydalanuvchilar = ['admin', 'user', 'new', 'dark', 'salom']
#login = str(input("Iltimos loginni kiriting\n>>>"))
#if login in foydalanuvchilar:
#    print("Ushbu login band. Iltimos yangi login tanlang")
#else:
#    print("Xush kelibsiz", login.title())


son = int(input("istalgan butun sonni kiriting\n>>>"))
for n in range(2, 11):
    if not (son % n):
        print(f"{son} soni {n} soniga qoldiqsiz bo'linadi")