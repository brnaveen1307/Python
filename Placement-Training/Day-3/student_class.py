class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

student1 = Student("Naveen", 20)

student1.display_info()