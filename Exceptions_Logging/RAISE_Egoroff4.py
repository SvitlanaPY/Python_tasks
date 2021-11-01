"""
Інструкція raise дозволяє в любий момент нашого коду викликати виключення, для цього потрібно написати
raise <exception>
де exception - це або вбудований клас помилки/клас виключення(KeyError, IndexError, TypeError, тощо):
raise IndexError
або це об"єкт класу Exception:
a = IndexError()
raise a
Під час ініціалізації помилки, ми можемо вказувати текст помилки:
aa = TypeError("Помилка типу"), а у цієї змінної aa є атрибут args і в нього будуть поступати всі значення, які ми будемо передавати в момент ініціалізації:
b = TypeError(1, 2, 3, 4)
b.args
"""
print("1. ", "- "*20)
b = TypeError(1, 2, 3, 4)
print(b.args)   # (1, 2, 3, 4)
print(repr(b))   # TypeError(1, 2, 3, 4)

# raise Exception("BIG error", 1, 3, 2)
# # Exception: ('BIG error', 1, 3, 2)

"""
Інколи виникають такі ситуації, коли нам потрібно перехопити помилку, зробити з нею щось, 
а потім вивести в консолі повідомлення про помилку, тобто зробити так, щоб потік виключення потрапив знову в консоль,
а для цього потрібно її викликати.
"""
print("2. ", "-- "*20)
# try:
#     [1, 2, 3][10]
# except (KeyError, IndexError) as err:
#     print(f"E R R O R:  {repr(err)}")
#     raise
#
# # E R R O R:  IndexError('list index out of range')
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 30, in <module>
# #     [1, 2, 3][10]
# # IndexError: list index out of range
# #
# # Process finished with exit code 1


print("3. ", "-- "*20)
"""
Можемо перехоплювати один тип виключень, а викликати зовсім інший тип виключення, 
але Traceback буде містит всі ті типи виключень, які трапились:
"""
# try:
#     [1, 2, 3][10]
# except (KeyError, IndexError) as err:
#     print(f"E R R O R:  {repr(err)}")
#     raise TypeError
#
# # E R R O R:  IndexError('list index out of range')
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 45, in <module>
# #     [1, 2, 3][10]
# # IndexError: list index out of range
# #
# # During handling of the above exception, another exception occurred:
# #
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 48, in <module>
# #     raise TypeError
# # TypeError


"""
Якщо ми не хочемо бачити в Traceback ті виключення, які перехоплюємо/обробляємо, а лише ті виключення, які викликаємо,
тоді потрібно написати інструкцію from None:
 
"""
print("4. ", "+ "*20)
# try:
#     [1, 2, 3][10]
# except (KeyError, IndexError) as err:
#     print(f"E R R O R:  {repr(err)}")
#     raise TypeError("Own error raised from nothing.") from None
#
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 77, in <module>
# #     raise TypeError("Own error raised from nothing.") from None
# # TypeError: Own error raised from nothing.


print("5. ", "= "*20)
# try:
#     raise ValueError("Помилка значенн - ValueError")
# except ValueError:
#     try:
#         raise TypeError("Помилка типу - TypeError")
#     except TypeError:
#         raise Exception("Велике виключення")
#
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 87, in <module>
# #     raise ValueError("Помилка значенн - ValueError")
# # ValueError: Помилка значенн - ValueError
# #
# # During handling of the above exception, another exception occurred:
# #
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 90, in <module>
# #     raise TypeError("Помилка типу - TypeError")
# # TypeError: Помилка типу - TypeError
# #
# # During handling of the above exception, another exception occurred:
# #
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 92, in <module>
# #     raise Exception("Велике виключення")
# # Exception: Велике виключення


"""
Помилки TypeError("Помилка типу - TypeError") не буде в Traceback
"""
print("6. ", "** "*20)
try:
    raise ValueError("Помилка значенн - ValueError")
except ValueError as first:
    try:
        raise TypeError("Помилка типу - TypeError")
    except TypeError as second:
        raise Exception("Велике виключення") from first

# Traceback (most recent call last):
#   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 117, in <module>
#     raise ValueError("Помилка значенн - ValueError")
# ValueError: Помилка значенн - ValueError
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/RAISE_Egoroff4.py", line 122, in <module>
#     raise Exception("Велике виключення") from first
# Exception: Велике виключення
