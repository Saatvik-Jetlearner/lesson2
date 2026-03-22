class school:
    def __init__(self, name, grade, school_name):
        self.name = name
        self.grade = grade
        self.school_name = school_name

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_grade(self):
        return self.grade
    def get_school_name(self):
        return self.school_name
    
    def showStudent(self):
        print("Hello, I am a student named {}, in grade {}, attending {}".format(self.name, self.grade, self.school_name))

student1 = school("Jack", "10th", "Greenwood High")
student1.showStudent()
print(student1.get_name())

student1.set_name("John")
student1.showStudent()

student2 = school("Emily", "11th", "Greenwood High")
student2.showStudent()
student2.set_name("Emma")
student2.showStudent()
