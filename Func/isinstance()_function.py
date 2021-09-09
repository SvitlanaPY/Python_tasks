# 4*. Check the type of the objects by using isinstance.
def type_definition(v):
    if isinstance(v, str):
        print('type is str')
    elif isinstance(v, int):
        print('type is int')
    elif isinstance(v, list):
        print('type is list')
    elif isinstance(v, dict):
        print('type is dict')
    elif isinstance(v, set):
        print('type is set')
    elif isinstance(v, tuple):
        print('type is tuple')
    elif isinstance(v, float):
        print('type is float')

type_definition(int_a)    # OUTPUT: type is str
type_definition(str_b)    # OUTPUT: type is int
type_definition(set_c)    # OUTPUT: type is set
type_definition(lst_d)    # OUTPUT: type is list
type_definition(dict_e)   # OUTPUT: type is dict
