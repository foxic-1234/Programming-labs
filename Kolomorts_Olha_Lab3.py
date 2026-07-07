print('Програмування. Частина 2. Лаботаротна робота №3, Коломоєць Ольги ФБ-44 Варіант 9')
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}  
    
    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name}\nОцінки: {self.grades}"
    
    def add_grades(self, semester, grades_list):
        if semester in self.grades:
            self.grades[semester].extend(grades_list)
        else:
            self.grades[semester] = grades_list
    
    def average_grade(self, semester):
        if semester in self.grades and self.grades[semester]:
            return sum(self.grades[semester]) / len(self.grades[semester])
        return 0 
    
    def overall_average(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def best_semester(self):
        if not self.grades:
            return None
        return max(self.grades, key=lambda sem: self.average_grade(sem))

    def worst_semester(self):
        if not self.grades:
            return None
        return min(self.grades, key=lambda sem: self.average_grade(sem))

student = Student("Софія", "Шевченко")
student.add_grades("Осінь 2023", [90, 85, 88, 92])
student.add_grades("Весна 2024", [75, 80, 78, 85])
student.add_grades("Осінь 2024", [95, 90, 92, 94])

print(student)
print("Середній бал за Весна 2024:", student.average_grade("Весна 2024"))
print("Загальний середній бал:", student.overall_average())
print("Найкращий семестр:", student.best_semester())
print("Найгірший семестр:", student.worst_semester())
