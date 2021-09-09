# Напишите программу, которая отсортирует список subject_marks по возрастанию оценок.
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
#
# Sample Input:
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
# Sample Output:
# History 82
# English 88
# Science 90
# Physics 93
# Maths 97

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
b = sorted(subject_marks, key=lambda marks: marks[1])
print(b)   # [('History', 82), ('English', 88), ('Science', 90), ('Physics', 93), ('Maths', 97)]
for i in b:
    print(*i)


print()
# Напишите программу, которая отсортирует список subject_marks по убыванию оценок.
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
# Sample Input:
# subj_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# Sample Output:
# Maths 97
# Physics 93
# Programming 91
# Science 90
# English 88
# History 82
# French 78
# Chemistry 76
# Art 58

subj_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]

b = sorted(subj_marks, reverse=True, key=lambda marks: marks[1])
for i in b:
    print(*i)


print()
# Напишите программу, которая отсортирует список subject_marks по убыванию оценок.
# Предметы, имеющих одинаковые оценки, должны быть отсортированы в алфавитном порядке
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
#
# Sample Input:
# s_m = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# Sample Output:
# Physics 93
# Programming 91
# Science 90
# Chemistry 88
# English 88
# Maths 88
# Art 78
# French 78
# History 78
s_m = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
s_m = sorted(s_m, key=lambda marks: (-marks[1], marks[0]))
# s_m = sorted(s_m, key=lambda x: x[0])
# s_m = sorted(s_m, key=lambda x: -x[1])
for i in s_m:
    print(i[0], i[1])
