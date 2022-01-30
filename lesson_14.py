# Lesson 14
# Shokhrukh Shirinboev
# Diciontary
# January 23, 2022

#eng_uz = {"apple" : "olma", "apricot" : "o'rik", "banana" : "banan"}
#print(eng_uz)
#print(eng_uz["apple"])


#friend = {'name' : "suhrob", 'surname' : "mamirzaev", 'address' : "samarkand", 'age' : "20"}
#print (friend)
#print (f" My friend is {friend['name'].title()}, \
#his surname is {friend['surname'].title()},\
#he is from {friend['address'].title()},\
#he is {friend['age']} years old ")

#food = {'Mehroj' : 'palov', 'Dilmurod' : 'manti', 'Ahror' : 'somsa', 'Azizbek' : 'kabob', 'Ravshan' : 'chuchvara'}
#print (f"Mehrojning sevimli taomi {food['Mehroj']}")
#print (f"Ahrorning sevimli taomi {food['Ahror']}")
#print (f"Ravshanning sevimli taomi {food['Ravshan']}")

# Python izohli lug`ati - PIL

pil = {'if' : 'agar', 'elsa' : 'aks holda', 'integer' : 'butun son', 'float' : 'haqiqiy son', 'string' : 'belgili ifoda', 'true' : 'rost ifoda', 'list' : "ro'yxat", 'false' : "yolg'on"}
word = input(str("so'zni kiriting \>>>"))
#print("Ushbu so'zning izohi")
#print(pil.get(word,"Bunday so'z mavjud emas"))

izoh = pil.get(word)
if izoh==None:
    print("bunday so'z mavjud emas")
else:
    print(f"{word.title()} so'zi {izoh} deb tarjima qilinadi")
