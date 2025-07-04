message = 'Toi ten la nguyen huu phuoc dep trai never die'
count = {}
for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1
print(count)