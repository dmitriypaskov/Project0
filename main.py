import Student
import Group
import TooManyStudentsError

st1 = Student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
for i in range(11):
    try:
        gr.add_student(Student.Student('Male', 30, 'Steve', 'uobs', 'AN142'))
    except TooManyStudentsError.TooManyStudentsError as e:
        print(e)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
# gr.delete_student('Taylor')
print(gr)  # Only one student
print(gr.count())
print("Ok")
