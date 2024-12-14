# Importa la clase correctamente
from school.Student import Student

student = Student("Ana", "Perez", 20, "Engineering", 8.5)
print(student)

student.set_major("Teacher")
student.set_first_name("Viviano")
print(student)