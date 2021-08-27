class BadName(Exception):
    pass

def greeting(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(f'{name} -- is inappropriate name')

print(greeting("Anton"))
print(greeting("anton"))