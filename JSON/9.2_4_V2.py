# В этой задаче вам необходимо раскодировать текст, находящийся в данном текстовом файле.
# Ключ для декодирования располагается в json-файле.
# В качестве ответа нужно просто отправить получившийся текст.
# И обратите внимание, что раскодировать нужно только лишь буквы,
# все остальные символы (цифры, знаки пунктуации и т.д.) необходимо выводить как есть.

import json

with open("Alphabet.json", "r", encoding="utf-8") as file, open("Abracadabra.txt", "r") as file_txt, open("new_text_v2.txt", "w") as new_file:
    dict_ = json.load(file)   # dict
    text = file_txt.read()   # str
    new_text = ''
    for letter in text:
        new_text = new_text + dict_.get(letter, letter)   # dict_.get(letter,  = dict_[letter]
        # print(dict_[letter])
        # print(letter)
    new_file.write(new_text)
    print(new_text)
    # print(repr(new_text))


# print(data)
# print(type(data))
# print(text)
# print(type(text))
