#Tro choi keo bua bao
import random, sys
thang = 0
thua = 0
hoa = 0
while True:
    print('Ti so: %s Thang, %s Thua, %s Hoa' % (thang, thua, hoa) )
    while True:
        print('Hay chon keo, bua, bao')
        print('Hoac exit de thoat chuong trinh')
        nguoiChoi = input('> ')
        if nguoiChoi == 'exit':
            sys.exit()
        if nguoiChoi in ['keo', 'bua', 'bao']:
            break
        else:
            print('Nhap sai moi nhap lai')

    may = random.randint(1, 3)
    if may == 1:
        may = 'keo'
        print(nguoiChoi, 'vs', may) 
    elif may == 2:
        may = 'bua'
        print(nguoiChoi, 'vs', may) 
    elif may == 3:
        may ='bao'
        print(nguoiChoi, 'vs', may) 

    if nguoiChoi == may:
        print('Ket qua hoa')
        hoa = hoa + 1
    elif nguoiChoi == 'keo' and may == 'bua':
        print('Ban da thua')
        thua = thua + 1
    elif nguoiChoi == 'bua' and may == 'keo':
        print('Ban da thang')
        thang = thang + 1
    elif nguoiChoi == 'bua' and may == 'bao':
        print('Ban da thua')
        thua = thua + 1 
    elif nguoiChoi == 'bao' and may == 'bua':
        print('Ban da thang')
        thua = thang + 1  
    elif nguoiChoi == 'bao' and may == 'keo':
        print('Ban da thua')
        thua = thua + 1
    elif nguoiChoi == 'keo' and may == 'bao':
        print('Ban da thang')
        thang = thang + 1
    




