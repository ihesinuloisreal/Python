Student_score = {
    "Harry": 91,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
Student_grade = {}

for key in Student_score:
    score = Student_score[key]
    if score >= 91 and score <= 100:
        Student_grade[key] = "Outstanding"
    elif score >= 81 and score <= 90:
        Student_grade[key] = "Exceeds Expectation"
    elif score >= 71 and score <= 80:
        Student_grade[key] = "Acceptable"
    elif score <= 70:
        Student_grade[key] = "Fail"

print(Student_grade)
