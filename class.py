def is_president(person):
    if person == "김한준" or person == "한준" :
        return True
    else :
        return False

is_president("한준")
   
def make_president():
    print = input("이름을 입력해주세요: ")

    if is_president(person):
        if person == "김한준":
            return make_two_letter_likelion(person)
        else :
            return make_likelion(person)
    else:
        print("회장아님 ㅋ")

make_president()


