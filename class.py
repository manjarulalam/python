class Classname:
    name = 'test class'


class Student:
    student_name = 'Manjarul'
    student_roll = 2345

v = Classname()
a = Student()
print(a.student_name)
print(v.name)




class Classname:
    name = "Hasan"
class Student:
    student_name = "Foyez"
    student_roll = "77858"
b = Student
print(b.student_roll)    
a = Classname
print(a.name)




class Students:
    __student_name = "Manjarul Alam"
    student_roll = "679236"

    def get_student_name(self):
        return self.__student_name
    
x=Students()
print(x.get_student_name())



class student:
    def __init__(self, name, roll):
        self.name = name
        st = Students(name="Tamim",Roll = 65)
        st2 = Students("Hamim",87)
        print("Name----Roll")
        for item in [st, st2]:
         print(f"{item.name,item.roll}")





