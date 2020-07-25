# 2 part of the 1 ex
with open('111.txt', 'r+') as file, open('new_file.txt', 'w+') as file2:
    data = file.read()
    file2.write(data)



# 3 part of the 1 ex
with open('111.txt', 'r+') as file:
    data = file.read()
    file.write('This is the end!\n')
with open('111.txt', 'r') as file:
    print(file.read())
file.close()




