def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))

append_to_list(77)
append_to_list(88)
append_to_list(99)
