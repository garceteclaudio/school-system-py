# Importa la clase correctamente
from school.Student import Student
from school.Professor import Professor
from school.Class import Class

student1 = Student("Ana", "Perez", 20, "Engineering", 8.5)
print(student1)
student1.set_first_name("Pancracia")
student1.set_last_name("Eusebia")
student1.set_age(15)
print(student1)

student2 = Student("Abraham", "Josebio", 22, "Construction worker", 7.5)
print(student2)

professor = Professor("Pepe", "Fentozler", 40, "Mathematics",20)
print(professor)


# Create a class and add students
math_class = Class("Math 101", professor)
math_class.add_student(student1)
math_class.add_student(student2)

# Assign subjects to students
math_class.assign_subject("Algebra", student1)
math_class.assign_subject("Calculus", student2)

# Print class information
print(math_class)

# Get subjects for a student
print(f"Subjects for {student1.first_name}: {math_class.get_subjects_for_student(student1)}")