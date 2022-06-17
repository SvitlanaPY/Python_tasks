"""
Инициалы
Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека
Вам необходимо вывести фамилию и инициалы, как в примерах ниже

Sample Input 1:
Марина Денисовна Климова
Sample Output 1:
Климова М.Д.

Sample Input 2:
Марк Ильич Воробьев
Sample Output 2:
Воробьев М.И.
"""

name, midname, surname = input().split()
name = name.replace(name, name[0]) + '.'
print(name)
midname = midname.replace(midname, midname[0]) + '.'
print(surname, name + midname)


# №2:
# name, midname, surname = input().split()
# print(f'{surname} {name[0]}.{midname[0]}.')
