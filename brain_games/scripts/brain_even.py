import random
from brain_games import main


name = main()
print('Answer "yes" if the number is even, otherwise answer "no"')
counter = 0


while counter < 3:
    number = random.randint(1, 1000)
    print(number)
    a = input('Your answer:')
    if (a == 'yes' and number % 2 == 0) or (a == 'no' and number % 2 == 1):
        print('Correct!')
        counter += 1
    elif (a != 'no' and number % 2 == 1):
        print("'{m}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,".format(m = a), name)
        counter = 4
    elif (a != 'yes' and number % 2 == 0):
        print("'{m}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,".format(m = a),name)
        counter = 4

if counter == 3:
    print('Congratulations!') 




