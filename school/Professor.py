from .Person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, subject, years_of_experience):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.years_of_experience = years_of_experience

    def __str__(self):
        return super().__str__() + f", Subject: {self.subject}, Years of Experience: {self.years_of_experience}"

    def teach(self):
        print(f"{self.first_name} is teaching {self.subject}.")