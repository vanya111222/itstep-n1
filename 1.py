'''class Student:
 print("Hi")'''

'''class Student:
 def __init__(self, height=165):

    self.height = height
    Student.amount_of_students +=1
 first_student = Student()
viktor = Student(height=180)
print(first_student.height)
print(viktor.height)'''
'''class Student:
    height = 160
        def __init__(self):
            self.height = 160

        def grow(self):
            print(self.height)
                self.height+=10
nick = Student()
kate = Student()
nick.printer()
kate.printer()'''
class Student:
 amount_of_students = 0
def __init__(self, height=160):
            self.height = height
 Student.amount_of_students+=1
def grow(self, height=1):
        self.height+=height
nick = Student()
print(nick.height)
kate = Student(height=170)
print(kate.height)
nick.grow(height=15)
print(kate.height)
print(nick.height)