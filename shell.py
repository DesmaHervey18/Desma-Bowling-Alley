def welcome():
    print('~*~*~*~*Welcome to Desma\'s Amazing Bowling Alley~*~*~*~*~*~* \n')
    response = input('Are you bowling alone today?\n')
    if response == 'yes':
        size = float(input('what is your size?\n'))
    elif response == 'no':
        print('Thank You for coming, Good day')


def Bowling_Alley():
    choice = (input('Are you ready to bowl?\n'))
    choice == 'yes'
    print('ok, Let\'s get started...')
    frame = 0
    total = 0
    for i in range(10):
        print('_______________________________________________')
        ball_1, ball_2 = 0, 0
        ball_1 = int(input('\nWhat did you roll on the first roll? '))
        frame = frame + 1
        if ball_1 == 10:
            print('~~**~STRIKE~**~~')
        elif ball_1 < 10:
            print('**SPARE**')
            ball_2 = int(input('\nHow many pins fell on your roll? '))
        print('\nFRAME:{}'.format(frame))
        total += (ball_1 + ball_2)
    print('Player Score: {}'.format(total))


# def bowler():
#     total = 0
#     for frame in frames:
#         total += sum(frames)
#         print(total)
#     print(frame)


def main():
    welcome()
    Bowling_Alley()


if __name__ == '__main__':
    main()
