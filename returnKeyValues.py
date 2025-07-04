spam = {'name' : 'Phuoc', 'age' : 20, 'job' : 'student'}
print(spam)
for i in spam.values():
    print(str(i))
print('')
for i in spam.keys():
    print(i)
print('')
for i in spam.items():
    print(i)
print('')
for k, v in spam.items():
    print(k + ': ' + str(v))