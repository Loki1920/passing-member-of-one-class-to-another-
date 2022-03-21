#passing member of one class to another 
class Student:
  def __init__(self,n,r):
    self.name = n
    self.roll = r
  def disp(self):
    print("student name:",self.name)
    print("student roll:",self.roll)

class User:
  @staticmethod
  def show(s):
    print("user name:",s.name)
    print("user roll:",s.roll)
    s.disp()

stu = Student('Rahul',101)
User.show(stu)