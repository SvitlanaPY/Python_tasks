# В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут,
# после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.
# Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
# Выведите два целых числа: время окончания урока в часах и минутах.

# n = int(input())
lessons_num = 6
parn_lesson = 0
neparn_lesson = 0
for k in range(1, lessons_num):
    if k % 2 == 0:
        neparn_lesson += 1
    else:
        parn_lesson += 1
print(f"Парних уроків є {parn_lesson}, а непарних уроків є {neparn_lesson}")
# print("Парних уроків є {}, а непарних уроків є {}".format(parn_lesson, neparn_lesson))
total_time = lessons_num * 45 + parn_lesson * 5 + neparn_lesson * 15
hrs = total_time // 60 + 9
mins = total_time % 60
print(hrs, mins)   # 14 15
