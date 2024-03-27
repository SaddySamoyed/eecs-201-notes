
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def passing(self):
        return self.grade >= 70.0

    def __str__(self):
        return f"{self.name} - {self.grade}"

if __name__ == '__main__':
    # Example test case for the Student class
    student1 = Student('Bob', 84)
    print(student1)  # Expected: Bob - 84

    # Testing the passing() method
    print(student1.passing())  # Expected: True
