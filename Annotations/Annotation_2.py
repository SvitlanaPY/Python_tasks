"""
Annotation - це такий інструмент, що дозволяє зробити наш код більш інформативним і
позбутись деяких проблем, пов"язаних із динамічною типізацією.

Щоб зробити аннотації для якоїсь колекції з вказанням аннотації для її елементів, потрібно використати модуть typing.
Всередині можуля typing є багато ін колекцій, таких як:
Dict, Tuple, List...

def list_upper(lst_t: List[str]):
    for elem in lst_t:
        print(elem.upper())
"""
from typing import List, Dict


def list_upper(lst_t: List[str]):   # аннотація функції
    for elem in lst_t:
        print(elem.upper())


a = ['hello', 'hi', 'good-morning']
list_upper(a)

# аннотація змінної:
# a: List[str] = ['hello', 'hi', 'good-morning']
# d: Dict[str, int] = {'a': 100, 'b': 200}
