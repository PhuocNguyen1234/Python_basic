name = ''
while not name:
    name = input('Nhap vao ten:')
print('Nhap vao so luong khach: ')
soKhach = int(input('> '))
if soKhach:
    print(f'{name} da dat {soKhach} phong')