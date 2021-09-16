import csv
#  csv - текстовий формат для табличних даних

with open("csv_data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open("tsv_data.tsv") as f_f:
    reader = csv.reader(f_f, delimiter="\t")
    for row in reader:
        print("tsv_data:", row)


# students = [
#     ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
#     ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
# ]
#
# with open("csv_data.csv", "a") as ff:
#     writer = csv.writer(ff)
#     writer.writerows(students)   # записуємо спиок students у файл "csv_data.csv" командою в один рядок writer.writerow(students),
#     # або проходячись в циклі for по елементах списку students (two code lines below)
#     for student in students:
#         writer.writerow(student)

# with open("csv_data.csv", "a") as fff:
#     writer = csv.writer(fff, quoting=csv.QUOTE_NONNUMERIC)   # open file to check it
#     # друга назва у QUOTE каже, що саме поміщати в ліпки: QUOTE_NONNUMERIC - всі НЕчислові значення поміщати в лапки
#     writer = csv.writer(fff, quoting=csv.QUOTE_ALL)   # open file to check it
#     writer.writerows(students)
#
# with open("csv_data.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# "csv_data file" contains:
# first name,last name,module1, module2,module3,description
# student,best,100,100,100,Excellent score
# student,good,90,"90,2",100,"Good score
# but could be better"
