class NonPositiveError(Exception):
    pass


x = int(input('Enter umber: '))
lst_ = []
while True:
    if x > 0:
        lst_.append(x)
        print(lst_)
        x = int(input('Enter umber: '))
    else:
        raise NonPositiveError("Negative number entered!")
