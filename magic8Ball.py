import random, sys
loiNhan = ['Xin chao cac ban', 'Hom nay ban khoe khong', 'Ban la ai', 'Ai la ban', 'Good luck!']
while True:
    print(loiNhan[random.randint(0, len(loiNhan) - 1)])
    traLoi = input('Nhap cau tra loi: ')
    if traLoi == 'Thoat':
        sys.exit()