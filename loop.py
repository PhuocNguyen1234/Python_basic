# name = ' '
# while name != 'Huu Phuoc':
#     name = input('Nhap vao ten cua ban: ')
# print('Chao mung Phuoc Nguyen')

# name = ''
# while True:
#     name = input('Nhap vao ten cua ban: ')
#     if name == 'Huu Phuoc':
#         print('Chao dai ca')
#         break

name = ''
while True:
    name = input('Nhap vao ten: ')
    if name != 'Phuoc Nguyen':
        continue
    else:
        password = input('Nhap vao mat khau:')
        if password == '123':
            print('Chao mung Phuoc Nguyen')
            break
        else:
            print('Dang nhap that bai')
            break
