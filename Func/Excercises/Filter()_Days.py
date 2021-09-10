# Напишите программу, которая отфильтрует список days так, чтобы в нем остались только дни,
# названия которых состоят из  четырех символов или начинаются с буквы S. Используйте при этом lambda функцию.
#
# Распечатайте получившийся список в алфавитном порядке, каждый элемент на новой строчке

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
filtered_days = list(filter(lambda x: len(x) == 4 or x.startswith('S'), days))
sorted_days = sorted(filtered_days)
print('\n'.join(sorted_days))
