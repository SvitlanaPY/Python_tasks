# Задача «Права доступа»
# В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам.
# Для каждого файла известно, с какими действиями можно к нему обращаться:
# запись W,
# чтение R,
# запуск X.
# В первой строке содержится число N — количество файлов содержащихся в данной файловой системе.
# В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами.
# Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл.
# К одному и тому же файлу может быть применено любое колличество запросов.
# Вам требуется восстановить контроль над правами доступа к файлам
# (ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция,
# или же Access denied, если операция недопустима.

# Inputs1:
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog
# Output1:
# OK
# Access denied
# Access denied
# OK
# OK
#
# Inputs2:
# 1
# abacaba X
# 3
# read abacaba
# write abacaba
# execute abacaba
# Output2:
# Access denied
# Access denied
# OK

n = int(input())
files_permissions = {}
for i in range(n):
    text = input().replace(' W', ' write').replace(' R', ' read').replace(' X', ' execute').split()
    key = text[0]
    files_permissions[key] = text[1:]
m = int(input())
for i in range(m):
    right, file = input().split()
    if right in files_permissions[file]:
        print('OK')
    else:
        print('Access denied')
