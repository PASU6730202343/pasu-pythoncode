class Student:
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    # Method to add a grade
    def add_grade(self, subject, grade):
        self.grades.append({"subject": subject, "grade": grade})

    # Method to get the average grade
    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(g['grade'] for g in self.grades)
        return total / len(self.grades)

    # Method to get the grade report
    def get_grade_report(self):
        report = ""
        for g in self.grades:
            report += f"{g['subject']}: {g['grade']}\n"
        return report.strip()


# สร้าง object และทดสอบ
student = Student("John", 20, "S123")

student.add_grade("Math", 85)
student.add_grade("Science", 92)

print(student.get_average_grade())  # ควรแสดง 88.5
print(student.get_grade_report())   # ควรแสดงรายงาน:
# Math: 85
# Science: 92