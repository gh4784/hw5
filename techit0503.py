# 함수(functions)
# 파라미터(매개변수), 인자(인수)


#name = 파라미터 
def print_name(name):
    print(f'이름은 {name}입니다')

# 지혜 = 인자(인수)
print_name("지혜")
print_name("민규")

def print_ex_string():
    print('예시 문자열 입니다.')

print_ex_string()

def print_name_age(name, age):
    print(f'이름은 {name}이고 {age}살 입니다.')

print_name_age("홍지혜","23")

#함수 기본값 세팅하기 (파라미터에 지정해주기)
def order_coffee(qty, option='hot'):
    print(f'{qty}잔/ {option}')

order_coffee(3, 'iced')
order_coffee(3)
order_coffee(option = 'iced', qty=5) #인자에 입력해주면 순서 바껴도 노상관

def get_id(email):
    email_id = email.removesuffix('@test.com')
    print(email_id)
    return email_id #user_id = get_id 데이터를 다른 영역에서 사용할 수 있을 것.

get_id('user@test.com')


def get_id(email):
    if email.endswith('@test.com'):
        email_id = email.removesuffix('@test.com')
        print(email_id)
    else :
        print('처리할 수 없는 이메일 주소입니다.')

user_id = get_id('user@example.com')


#클래스(classes) - 설계  대문자로 시작해야함

class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f'{self.name} 학생은 공부 중입니다.')

    def edit_major(self, new_major) : 
        student_1.major = new_major
        print(f'{student_1.major}로 전공이 변경되었습니다.')

#인스턴트 - 실체화된 사물
student_1 = Student('김멋사', '컴공과')

student_1_name = student_1.name
print(student_1_name)

student_1_graduated = student_1.is_graduated
print(student_1_graduated)
student_1.study()

student_1.edit_major('기계공학과')
#student_1.major = '기계공학과'
#print(student_1.major)




#클래스(classes) - 설계  대문자로 시작해야함

class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f'{self.name} 학생은 공부 중입니다.')

    def edit_major(self, new_major) : 
        student_1.major = new_major
        print(f'{student_1.major}로 전공이 변경되었습니다.')

#인스턴트 - 실체화된 사물
student_1 = Student('김멋사', '컴공과')

student_1_name = student_1.name
print(student_1_name)

student_1_graduated = student_1.is_graduated
print(student_1_graduated)
student_1.study()

student_1.edit_major('기계공학과')
#student_1.major = '기계공학과'
#print(student_1.major)



#상속 (Inheritance)

class ForeignStudent(Student):
    def __init__(self, name, major, country):
        super().__init__(name, major)
        self.country = country

#오버라이딩
    def study(self):
        print(f'{self.name} is studying now.')
       
foreign_stud_1 = ForeignStudent('홍지혜', '국문', 'USA')
print(foreign_stud_1.name)
print(foreign_stud_1.major)
print(foreign_stud_1.country)
print(foreign_stud_1.is_graduated)
foreign_stud_1.study()

