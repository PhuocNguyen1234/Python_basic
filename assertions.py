import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
ages = [26, 9, 10,1, 76, 73]
ages.reverse()
print(ages)
assert ages[0] <= ages[-1]
