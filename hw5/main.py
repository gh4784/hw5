import datetime


def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y-%m-%d')

    users = []

    while True:

        user = {}

        import re

        while True:
            username = input('ID(한글 2~4자): ')
            if re.match('[가-힣]{2,4}$', username):
                break
            else:
                print('잘못된 형식입니다.')

        while True:
            password = input(
                'PW(영문 대문자로 시작, 8글자 이상, 특수문자 (!, @, #, $) 중 1가지 반드시 포함): ')
            if len(password) >= 8 and password[0].isupper() and re.search(
                    "[!@#$]", password):
                break
            else:
                print('잘못된 형식입니다.')

        while True:
            email = input('EMAIL: ')
            if not (re.match("([\w\.-]+)@([\w\.-]+)(\.com+)", email)):
                print("잘못된 형식입니다.")
            else:
                break

        user['username'] = username
        user['password'] = password
        user['email'] = email
        user["stnr_date"] = stnr_date

        users.append(user)
        print([user['username'], user['password'], user['email']])

        print('정보를 추가로 입력하시겠습니까?')
        another_input = input('y or n >> ')
        another_input = another_input.lower()

        if another_input == 'y':
            pass
        elif another_input == 'n':
            exit()

def load_to_txt(user_list):
        f = open('memberdb.txt', 'w', encoding='UTF-8')
        f.close()

def run:

        user_list = create_membership()
        load_to_txt(user_list)

run()
