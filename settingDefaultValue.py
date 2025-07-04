spam = {'name' : 'Phuoc', 'age' : 20, 'skill' : 'sleep'}
print(spam)
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)
spam.setdefault('height', 60)
print(spam)