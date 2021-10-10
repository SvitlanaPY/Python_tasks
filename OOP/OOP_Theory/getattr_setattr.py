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
    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(101, 'Jim')
setattr(student, 'email', 'email_1@gmail.com')
student_email = 'email_2@gmail.com'        # create 'student_email' variable
setattr(student, 'email', student_email)
print('student.email=', getattr(student, "email"))
# OUTPUT: student.email= email2@gmail.com
