import random, sys
def yesOrNo(question):
    if question == 1:
        print('Ban on chu?')
    elif question == 2:
        print('Ban la con trai phai khong?')
    elif question == 3:
        print('Ban an sang roi phai khong?')
while True:
    q = random.randint(1, 3)
    yesOrNo(q)
    answer = input('> ')
    if answer == 'Cút':
        sys.exit()


