from string import ascii_lowercase
# print(ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz

letters = ascii_lowercase
alphabet = {}
for i in range(1, len(letters) + 1):
    alphabet[letters[i-1]] = i
print(alphabet)


# (2):
# alphabet = {}
# i = 0
# for val in ascii_lowercase:
#     alphabet.setdefault(val, i)   # alphabet[val] = i
#     i += 1
#     print(val, i)


# (3):
# for key, val in alphabet.items():
#     print(key, val)
