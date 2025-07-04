import sys
birthdays = {'Phuoc' : '20/6', 'Nam' : '21/6', 'Trung' : '20/9'}
while True: 
    print('Nhap vao ten de xem ngay sinh nhat (Enter de thoat) ')
    name = input('> ')
    if name == '':
        sys.exit()
    if name in birthdays:
        print('Ngay sinh nhat cua ' + name + ' la ' + birthdays[name])
    else:
        print('Khong tim thay ten ' + name)
        print('Moi nhap vao ngay sinh nhat cua ' + name + ' vao tu dien')
        bday = input('> ')
        if bday == '':
            continue
        birthdays[name] = bday
        print('Du lieu da duoc update')