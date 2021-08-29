# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# Программа получает на вход числа n(km_day) и m(rout_length).

from math import *
# km_day = int(input())
km_day = 483
# rout_length = int(input())
rout_length = 9382
x = ceil(rout_length / km_day)
print(f"Чтобы проехать маршрут длиной {rout_length} километров, нужно {x} дней")
