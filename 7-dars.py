# 1, 2-mashqlar
#friends = ['Dilmurod', 'Ahror', 'Mehroj', 'MM']
#print ("Salom", friends[0].title(), "qandaysan")
#print ("Nima yanngiliklar", friends[1].title())
#print ("Ha", friends[2].title(), "garri nima gap")
#print ("kurinmaysan hech", friends[-1].upper())

# 3, 4-mashqlar
#sonlar = [151, 7884, 58, 3554, -587, 65.8]
#print (sonlar[0] + sonlar[2])
#print (sonlar)
#sonlar[0] = 2
#print (sonlar)
#del sonlar[-1]
#print(sonlar)
#print(sonlar[-2])

# 5, 6-mashqlar
#t_shaxslar = ["Rockfeller", "Pushkin", "Gitler"]
#z_shaxslar = ["Mask", "Putin", "Ronaldu"]
# print ("Men tarixiy shaxsladadn", t_shaxslar[-1], "va zamonaviy shaxslardan", z_shaxslar[1], "bilan suhbat qurishni istar edim")
#t_shaxs = t_shaxslar.pop()
#z_shaxs = z_shaxslar.pop(1)
#print ("men " + t_shaxs + " v " + z_shaxs + " ni hurmat qilaman ")

# 7, 8, 9, 10-mashqlar
friends = []
friends.append("Suhrob")
friends.append("Jalol")
friends.append("Komronbek")
friends.append("Mehroj")
friends.append("Ahror")
friends.append("Dilmurod")
friends.remove("Jalol")
friends.remove("Suhrob")
friends.append("Abulqosim")
friends.insert(0, "Muhammad")
friends.insert(3, "Sobirxon")
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(3))
print("\n Kelgan mehmonlar:", mehmonlar)
print("\n Kelmaganlar:", friends)