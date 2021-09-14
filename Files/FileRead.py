# Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
# Учитывайте, что содержимое файла может быть как на русском языке, так и на английском

def file_read(file_name):
    file = open(file_name, 'r', encoding='UTF-8')
    print(file.read())
    file.close()

file_read('111.txt')
