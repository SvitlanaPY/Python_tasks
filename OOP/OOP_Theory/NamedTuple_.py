"""
NamedTuple - це
"""
# Create the same class (6) but using NamedTuple

from collections import namedtuple
AddressBookNamedTuple = namedtuple('AddressBookNamedTuple', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
ab = AddressBookNamedTuple('10', 'John Smith', '(888) 558-9004', '123 Main St, Pasadena, CA', ' jsmith@comcast.net', '01 January 2000', '21')
print(ab)
# OUTPUT: AddressBookNamedTuple(key='10', name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age='21')
print(ab[0:3])
# OUTPUT: ('10', 'John Smith', '(888) 558-9004')
print('address:', ab.address)
# OUTPUT: address: 123 Main St, Pasadena, CA
