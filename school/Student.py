from .Person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, major, average_grade):
        super().__init__(first_name, last_name, age)
        self.major = major
        self.average_grade = average_grade

    # Getters
    def get_major(self):
        return self.major

    # Setters
    def set_major(self, major):
        self.major = major

    def __str__(self):
        return super().__str__() + f", Major: {self.major}, Average Grade: {self.average_grade}"

    def study(self):
        print(f"{self.first_name} is studying {self.major}.")