"""Кнопочные гонки
Двое решили посоревноваться в набирании текстов на сайте «Кнопочные гонки».
Во время соревнования необходимо ввести текст из s символов.
Первый участник набирает один символ за v1 миллисекунд и имеет пинг t1 миллисекунд.
Второй участник набирает один символ за v2 миллисекунд и имеет пинг t2 миллисекунд.
При соединении с пингом (задержкой) в t миллисекунд соревнование проходит для участника следующим образом:
Ровно через t миллисекунд после начала соревнования участник получает текст, который необходимо ввести.
Сразу после этого он начинает вводить этот текст.
Ровно через t миллисекунд после того, как он перепечатал весь текст, сайт получает информацию об этом.
Победителем в соревновании является тот участник, информация об успехе которого пришла раньше.
Если информация пришла от обоих участников одновременно, считается, что произошла ничья.
По данной длине текста и информации об участниках, определите исход игры.

Входные данные
Первая строка содержит пять целых чисел s, v1, v2, t1, t2  (1 <= s,v1,v2,t1; t2 <= 1000) —
s - количество символов в тексте, v1 - скорость набора текста первым участником,
v2 - скорость набора текста вторым участником, t1 - пинг первого участника и t2 - пинг второго участника.

Выходные данные
Если выиграет первый участник, выведите «First».
Если выиграет второй участник, выведите «Second».
В случае ничьей выведите «Friendship».
Sample Input 1:
5 1 2 1 2
Sample Output 1:
First

Sample Input 2:
3 3 1 1 1
Sample Output 2:
Second

Sample Input 3:
4 5 3 1 5
Sample Output 3:
Friendship
"""
s, v1, v2, t1, t2 = map(int, input().split())
first = t1 + s * v1 + t1
second = t2 + s * v2 + t2
if first < second:
    print('First')
else:
    if second < first:
        print('Second')
    else:
        print('Friendship')