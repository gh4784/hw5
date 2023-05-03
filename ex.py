
print('추가로 입력하시겠습니까?')
another_input = input('y or n >> ')
another_input = another_input.lower()

if another_input == 'y':
    pass
elif another_input == 'n':
    exit()






from id_getter import get_id
user_id = get_id('user@test.com')
print(user_id)




while not register :
    print('회원가입을 진행하시겠습니까\ny:진행  N:취소')
    register_input = input('>> ')
    register_input = register_input.lower()

    if register_input == 'y' :
        register = True
        print('==================================')
        print('회원가입이 진행됩니다')
        print('==================================')
    elif register_input == 'n' :
        print('==================================')
        print('회원가입이 취소됩니다')
        print('==================================')
    else : 
        print('입력 값을 확인해주세요.')

