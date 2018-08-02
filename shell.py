def welcome():
    print('~*~*~*~*Welcome to Desma\'s Amazing Bowling Alley~*~*~*~*~*~* \n')
    while True:
        response = input('Do you want to bowl today?\n').upper().strip()
        if response == 'YES':
            break
        elif response == 'NO':
            print('Thank You for coming, Good day')
        else:
            print('*****Invalid Answer, Please Try Again*****')


def Bowling_Alley():
    choice = input('Are you ready to bowl?\n')
    if choice == 'YES':
        print('ok, Let\'s get started...')
        frame = 0
        total = 0
        for i in range(10):
            print('_______________________________________________')
            ball_1, ball_2 = 0, 0
            frame = frame + 1
            ball_1 = int(input('\nWhat did you roll on the first roll? '))
            if ball_1 == 10:
                print('~~**~STRIKE~**~~')
                continue

            ball_2 = int(input('\nHow many pins fell on your roll? '))
            if ball_1 + ball_2 == 10:
                print('**SPARE**')

            print('\nFRAME:{}'.format(frame))
            total += (ball_1 + ball_2)
        print('Player Score: {}'.format(total))
    elif choice == 'NO':
        exit()
    else:
        print('*****Invalid Answer, Please Try Again*****')


def main():
    welcome()
    Bowling_Alley()


if __name__ == '__main__':
    main()
