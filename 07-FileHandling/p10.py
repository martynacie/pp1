file = open('txt.txt', 'w')
file = file.write("name \nsurname \nuniversity \nfield")
file_content = file.read()
print(file_content)