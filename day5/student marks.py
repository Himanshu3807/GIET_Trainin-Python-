class Student:
    def _init_(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
    def validate_marks(self):
        return self._marks >= 0 and self._marks <= 100 
    def validate_age(self):
        return self.__age > 20  
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                return True
        return False  
    def set_student_id(self, id):
        self.__student_id = id
    
    def set_marks(self, marks):
        self.__marks = marks
    
    def set_age(self, age):
        self.__age = age
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_discount(self):
        if self.__marks > 65:
            return 0.25
        else:
            return 0
    def get_fee(self, course_fee):
        return (course_fee-(course_fee * self.get_discount()))
s = Student()
s.set_student_id(101)
s.set_marks(75)
s.set_age(23)
if s.check_qualification():
    print("Qualified for admission")
    course_fee = 10000
    fee_after_discount = s.get_fee(course_fee)
    print("Course fee after discount:", fee_after_discount)
else:
    print("Not qualified for admission")
