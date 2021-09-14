import pickle
# модуль для серилізації/десирилізації Python-об"єктів в двійковому форматі

# DUMPS (convert our list/str/dict... into byte-string)
list_111 = [1, 2, 3, 4, 5]
byte_data = pickle.dumps(list_111)
print(byte_data)   # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
print(type(byte_data))   # <class 'bytes'>

# LOADS (convert our byte-string with list/str/dict... from byte-string into list/str/dict...)
list_obj = pickle.loads(byte_data)
print(type(list_obj))   # <class 'list'>
print(list_obj)   # [1, 2, 3, 4, 5]



# ---------------------------------------------- #
# DUMP (save our converted list as byte-str into file "file_list1")
list_111 = [1, 2, 3, 4, 5]
file = open("file_list1", "wb")
pickle.dump(list_111, file)
# print(type(file))   # <class '_io.BufferedWriter'>
# print('type', type("file_list1"))   # type <class 'str'>
file.close()
# file1 = open("file_list1", "rb")
# print(file1.read())   # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
# file.close()

# LOAD
f_file = open("file_list1", "rb")
# in "file_list1" - serelized representation of our list_111
byte_obj = pickle.load(f_file)
print(type(byte_obj))   # <class 'list'>
print(byte_obj)   # [1, 2, 3, 4, 5]
file.close()




# DUMP / LOAD
print()
data = {
    'a': [1, 2.0, 3],
    'b': ("hello", "hi", "bye"),
    'c': {None, True, False}
}
with open("data_pickle", "wb") as f:
    pickle.dump(data, f)

# LOAD
with open("data_pickle", "rb") as ff:
    data_new = pickle.load(ff)
print("data_new: ", data_new)
# data_new:  {'a': [1, 2.0, 3], 'b': ('hello', 'hi', 'bye'), 'c': {False, None, True}}
