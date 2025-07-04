dsHocSinh = []
while True:
    ten = input('Nhap vao ten hoc sinh: ')
    if ten == '':
        break
    dsHocSinh = dsHocSinh + [ten]
print('Danh sach hoc sinh: ')
for i in dsHocSinh:
    print(i)

