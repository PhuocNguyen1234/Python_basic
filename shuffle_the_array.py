def numJewelsInStones(self, jewels, stones):
        jewls_set = set(jewels)
        count = 0
        for st in stones:
            if st in jewls_set:
                count += 1
        return count

print('Nhap jewels: ')
jewels = input('> ')
print('Nhap stones: ')
stones = input('> ')
print('So luong jewels trong stones la: ', numJewelsInStones(None, jewels, stones))