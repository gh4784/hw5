users = []

while True:

    user = {}

    username = input('ID: ')

    while True :
        password = input('PW: ')
        password_confirm = input('PW 확인 : ')
        if password == password_confirm :
            break
        else :
            print('패스워드가 일치하지 않습니다.')