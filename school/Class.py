class Class:
    def __init__(self, class_name, professor):
        self.class_name = class_name
        self.professor = professor    # The professor teaching the class
        self.students = set()         # Set of students (unique = No duplicate allowed)
        self.subjects = {}            # Dictionary of subjects and their corresponding students

    def add_student(self, student):
        """Add a student to the class."""
        self.students.add(student)
        print(f"{student.first_name} {student.last_name} has been added to {self.class_name}.")

    def remove_student(self, student):
        """Remove a student from the class."""
        if student in self.students:
            self.students.remove(student)
            print(f"{student.first_name} {student.last_name} has been removed from {self.class_name}.")
        else:
            print(f"Student {student.first_name} {student.last_name} not found in {self.class_name}.")

    def assign_subject(self, subject_name, student):
        """Assign a subject to a student."""
        if student not in self.subjects:
            self.subjects[student] = set()
        self.subjects[student].add(subject_name)
        print(f"{student.first_name} {student.last_name} has been assigned to {subject_name} in {self.class_name}.")

    def get_students(self):
        """Return a list of students in the class."""
        return [student.first_name + " " + student.last_name for student in self.students]

    def get_subjects_for_student(self, student):
        """Return the subjects for a specific student."""
        return self.subjects.get(student, "No subjects assigned.")

    def __str__(self):
        """Display information about the class."""
        student_list = ', '.join(self.get_students())
        return f"Class: {self.class_name}\nProfessor: {self.professor.first_name} {self.professor.last_name}\nStudents: {student_list}"