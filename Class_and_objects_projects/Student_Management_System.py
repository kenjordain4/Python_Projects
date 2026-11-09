


class Student:
  def __init__(self,name,student_id):
    self.name=name
    self.student_id=student_id
    self.grades=[]
  def add_grade(self,grade):
    self.grades.append(grade)

  def average_grade(self):
      if not self.grades:
          return 0
      return sum(self.grades) / len(self.grades)

  def is_passed(self):
      return self.average_grade() >= 21


  def display_info(self):
      status = "passed" if self.is_passed() else "not passed"
      return f"Student {self.name}, {self.student_id} is {status}"

class ClassRoom:
  def __init__(self,course_name):
      self.course_name=course_name
      self.students=[]

  def add_student(self,Student):
      self.students.append(Student)

  def display_all_students(self):
      for student in self.students:
          print(student.display_info())

  def get_top_student(self):
      if not self.students:
          return None
      return max(self.students, key=lambda x: x.average_grade())


s1 = Student("Alice", "S001")
s2 = Student("Bob", "S002")
s3 = Student("Charlie", "S003")

s1.add_grade(30)
s1.add_grade(40)

s2.add_grade(25)
s2.add_grade(35)

s3.add_grade(10)
s3.add_grade(20)


print(s1.average_grade())  # 35.0
print(s2.average_grade())  # 30.0
print(s3.average_grade())  # 15.0


print(s1.is_passed())  # True
print(s3.is_passed())  # False

classroom = ClassRoom("Python 101")


classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)

print('++++++Class info++++++++')

print(classroom.display_all_students())



top = classroom.get_top_student()

print("Top student:")
print(top.display_info())







