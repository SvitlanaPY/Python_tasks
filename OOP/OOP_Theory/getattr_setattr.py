print('\n########## 10 ##########')
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

stud = Student(101, 'Jim')
print("class name: ", Student.name)   # атрибут name класу Student
# class name:
print('class name is: ', getattr(Student, "name"))
# class name is:
print("class id: ", Student.id)
# class id:  0
print('class id is: ', getattr(Student, "id"))
# class id is:  0


print()
print("stud NAME: ", stud.name)   # атрибут name об"єкту stud
# stud NAME:  Jim
print('stud name is: ', getattr(stud, "name"))
# stud name is:  Jim
print("stud ID: ", stud.id)   # атрибут id об"єкту stud
# stud ID:  101
print('stud id is: ', getattr(stud, "id"))
# stud id is:  101


setattr(stud, 'email', 'email_1@gmail.com')
student_email = 'email_2@gmail.com'        # create 'student_email' variable
setattr(stud, 'email', student_email)
print('stud.email=', getattr(stud, "email"))
# OUTPUT: stud.email= email2@gmail.com

a = 'city'
student_city = 'Lviv'
setattr(stud, a, student_city)
print('stud.student_city=', getattr(stud, "city"))
print(stud.__dict__)
# {'id': 101, 'name': 'Jim', 'email': 'email_2@gmail.com', 'city': 'Lviv'}
