class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Getters
    def get_first_name(self):
        return self.first_name

    # Setters
    def set_first_name(self, first_name):
        self.first_name = first_name
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}"

    def greet(self):
        print(f"Hello, I am {self.first_name} {self.last_name}.")