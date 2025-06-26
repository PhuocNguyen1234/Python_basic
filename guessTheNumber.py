import random, sys
soBiMat = random.randint(1, 20)
print('Hay doan so bi mat da duoc chon ngau nhien tu 1 den 20')
print ('Ban chi co 5 co hoi de doan')
for i in range(1, 5):
    soDoan = int(input('Nhap so ban doan: '))
    if soDoan > soBiMat:
        print('So nay qua lon roi')
    if soDoan < soBiMat:
        print('So nay qua nho roi')
    else:
        print('Ban doan dung roi do la so: ', str(soBiMat))
        sys.exit()
print('Ban dã het 5 co hoi roi')
print('Dap an chinh xac la: ', str(soBiMat))
    