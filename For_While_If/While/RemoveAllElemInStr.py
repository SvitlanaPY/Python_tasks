s = input("Enter some text: ")
while len(s) > 0:
    letter = s[0]
    if 'z' >= letter >= 'a':
        print(letter, "- is small")
    elif 'Z' >= letter >= 'A':
        print(letter, "- is big")
    elif letter.isdigit():
        print(letter, "- is digit")
    else:
        print(letter, "- is some sign")
    s = s[1:]
    # print("s:", s)
