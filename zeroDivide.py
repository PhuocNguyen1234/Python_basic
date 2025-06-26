def spam(number):
        return 42 / number
try:    
    print(spam(2))
    print(spam(0))
    print(spam(1)) 
except ZeroDivisionError:
    print('Lỗi')       