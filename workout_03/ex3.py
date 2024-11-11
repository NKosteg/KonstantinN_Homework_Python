from student import Student
from course_group import CourseGroup

main_student = Student('Alex', 'Baldwin', 39, 'QA')
student_1 =Student('Anna', 'Ivanova', 30, 'QA')
student_2 = Student('Mark', 'Petrov', 25, 'QA')
student_3 = Student('Nina', 'Sidorova', 29, 'QA')
group_qa = CourseGroup(main_student.get_student(), [student_1.get_student(), student_2.get_student(),student_3.get_student()])

print(group_qa)
print()
print(f'{main_student.get_student()} учится вместе с: {group_qa.classmates}')

main_student.get_student()