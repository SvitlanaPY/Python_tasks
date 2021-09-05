# "Права доступа"
# Вася написал собственную операционную систему и теперь делает для нее систему прав доступа.
# Он решил, что в его системе будет 3 категории пользователей, обладающих разными правами:
# администраторы (admin) могут открывать и редактировать все файлы;
# опытные пользователи (experienced) могут открывать все файлы, кроме конфиденциальных (confidential),
# но не могут редактировать файлы с настройками (settings) и системные файлы (system)
# обычные пользователи (user) не могут открывать и/или редактировать конфиденциальные и системные файлы,
# а также файлы с настройками.
# Все категории пользователей могут открывать и редактировать обычные файлы (ordinary).
# При этом, если пользователь не имеет права открыть какой-либо файл,
# то, следовательно, он не имеет права его отредактировать.
#
# Напишите программу, которая сначала принимает имена файлов и их тип до символа точки, а затем запросы вида:
# имя_файла действие категория_пользователя.
# Действие может принимать одно из двух значений – read или edit,
# категория пользователя – одно из трех вышеперечисленных.
# После каждого действия программа должна выводить "Access granted" или "Access denied"
# в зависимости от успешности действия. Ввод запросов также происходит до точки.
#
# Sample Input:
# driver.drv system
# bussiness_data.txt confidential
# gtaV_graphics.txt settings
# отчет.txt ordinary
# fight_club.torrent ordinary
# facebook_users.db ordinary
# revenue_data.txt confidential
# top10_anime_titles.txt confidential
# best_coding_practices.pdf ordinary
# .
# driver.drv read admin
# revenue_data.txt read experienced
# gtaV_graphics.txt edit experienced
# отчет.txt edit admin
# отчет.txt read user
# fight_club.torrent read experienced
# facebook_users.db read user
# top10_anime_titles.txt read experienced
# .
# Sample Output:
# Access granted
# Access denied
# Access denied
# Access granted
# Access granted
# Access granted
# Access granted
# Access denied

dictt = {'admin': {'read': ['confidential', 'settings', 'system', 'ordinary'],
                   'edit': ['confidential', 'settings', 'system', 'ordinary']},
         'experienced': {'read': ['settings', 'system', 'ordinary'],
                         'edit': ['ordinary']},
         'user': {'read': ['ordinary'],
                  'edit': ['ordinary']}}
d = {}
while True:
    text = input()
    if text == '.':
        break
    file, file_type = text.split()
    d[file] = file_type
print("dict: ", d)
# d {'driver.drv': 'system', 'bussiness_data.txt': 'confidential', 'gtaV_graphics.txt': 'settings', 'отчет.txt': 'ordinary', 'fight_club.torrent': 'ordinary', 'facebook_users.db': 'ordinary', 'revenue_data.txt': 'confidential', 'top10_anime_titles.txt': 'confidential', 'best_coding_practices.pdf': 'ordinary'}
while True:
    text = input()
    if text == '.':
        break
    file, operation, role = text.split()
    # available_types = dictt[role][operation]
    if d[file] in dictt[role][operation]:
        print("Access granted")
    else:
        print("Access denied")
