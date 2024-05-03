class person: #parent class
    # assigning attributes
    def __init__(self, name, age, CID):
        self.name = name
        self.age = age
        self.CID = CID

    # defining behaviors / methods
    def walk(self):
        print(self.name, 'is walking')

    def talk(self):
        print(self.name, 'is talking')

    def sleep(self):
        print(self.name, 'is sleeping')

    def eat(self):
        print(self.name, 'is eating')

class teacher(person):
    def __init__(self, name, age, CID, subject, salary, department, designation):
        super().__init__(name, age, CID)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(self.name, 'is teaching')

    def grade_students(self):
        print(self.name, 'is grading')
        
    def attend_meeting(self):
        print(self.name, 'is attending meeting')


class student(person):
    def __init__(self, name, age, CID, std_id, course, year, gpa):
        super().__init__(name, age, CID)
        self.std_id = std_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(self.name, 'is studying')

    def attend_class(self):
        print(self.name, 'is in class')
        
    def write_exam(self):
        print(self.name, 'is writing exam')

t1 = teacher('tashi', 30, 12345, "accounts", 30000, "commerce", 'assistance')
t2 = teacher('dorji', 31, 12346, "physics", 20000, "commerce", "full teacher")

s1 = student("penjor", 18, 1111, 12345, "bbi", 1, 3)
s2 = student("tshering", 30, 1345, 123467, "bbi", 1, 3.4)

student_storage = [s1, s2]

for std in student_storage:
    print(std.name)
    print(std.gpa)
    print(std.course)
    print('=====')
