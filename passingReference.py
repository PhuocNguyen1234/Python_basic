import copy
def hello (mang):
    mang.append('Hello')

mang = ['Xin chao', 0, 1, 2]
hello(mang)
print(mang)
mang1 = copy.copy(mang)
mang1[1] = 'World'
print(mang)
print(mang1)
