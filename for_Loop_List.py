spam = ['cat', 'dog', 'bat', 'rat', 'lion', 'tiger']
for i in range(len(spam)):
    print('Index '+ str(i) + ' in spam is: ' + spam[i])
print('-------')
for index, item in enumerate(spam):
    print('Index ' + str(index) + ' in spam is: ' + item)
    