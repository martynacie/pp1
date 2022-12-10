produkt = input("dej produkta ")
file = open("shoping.txt","a")
file.write("\n"+ produkt)
file.close()