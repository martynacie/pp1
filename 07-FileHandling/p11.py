film_titlies = ["title1","title2","title3","title4","title5" ]
file = open('tities.txt', 'w')
for element in film_titlies:
        file.write(element + "\n")
file.close()