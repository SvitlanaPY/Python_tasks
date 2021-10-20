"""
Annotation - це такий інструмент, що дозволяє зробити наш код більш інформативним і
позбутись деяких проблем, пов"язаних із динамічною типізацією.

Щоб зробити аннотації для якоїсь колекції з вказанням аннотації для її елементів, потрібно використати модуть typing.
Всередині можуля typing є три важливі штуки, такі як як:
Optional, Any, Union

Можемо зробити аннотації для будь-якої змінної і записати їй тип Any:
a: Any = 12
а = "привіт"

Optional:
b: Optional[int] = None
означає, що змінна "b" може приймати значення або None(тобто бути порожньою) або int(цілого типу)

Union: за допомогою Union може об"єднувати кілька типів:
a: Union[int, float, str]
Тобто у змінну "а" може попадати будь-який тип із вказаних трьох (int, float, str)
В Python 3.10 запис a: Union[int, float, str] рівносильний запису:
a: int | float | str

"""
from typing import Optional, Any, Union


def add_numbers(a: Union[int, float, str], b: Optional[int] = None) -> int:
    return a + b


aa: Any = 12
аa = "привіт"

t: Optional[list] = [1, 23]
t: Optional[list] = None
