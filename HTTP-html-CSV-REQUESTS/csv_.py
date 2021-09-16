import csv
#  csv - текстовий формат для табличних даних

with open("csv_data.csv") as f:
    reader_obj = csv.reader(f)
    # print(reader_obj)   # <_csv.reader object at 0x7fb985c46040>
    # print(type(reader_obj))   # <class '_csv.reader'>
    for row in reader_obj:
        print(row)


# with open("tsv_data.tsv") as f_f:
#     reader_obj = csv.reader(f_f, delimiter="\t")
#     for row in reader_obj:
#         print("tsv_data:", row)


# students = [
#     ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
#     ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
# ]
#
# with open("csv_data.csv", "a") as ff:
#     writer_ = csv.writer(ff)
#     writer_.writerows(students)   # записуємо спиок students у файл "csv_data.csv" командою в один рядок writer.writerow(students),
#     # або проходячись в циклі for по елементах списку students (two code lines below)
#     for student in students:
#         writer_.writerow(student)

# with open("csv_data.csv", "a") as fff:
#     writer_ = csv.writer(fff, quoting=csv.QUOTE_NONNUMERIC)   # open file to check it
#     # друга назва у QUOTE каже, що саме поміщати в ліпки: QUOTE_NONNUMERIC - всі НЕчислові значення поміщати в лапки
#     writer_ = csv.writer(fff, quoting=csv.QUOTE_ALL)   # open file to check it
#     writer_.writerows(students)
#
# with open("csv_data.csv") as f:
#     reader_obj = csv.reader(f)
#     for row in reader_obj:
#         print(row)


# "csv_data file" contains:
# first name,last name,module1, module2,module3,description
# student,best,100,100,100,Excellent score
# student,good,90,"90,2",100,"Good score
# but could be better"
