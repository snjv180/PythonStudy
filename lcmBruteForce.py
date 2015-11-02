from itertools import count
for i in count(7):
    if all(map(lambda x: i % x == 0, range(1, 8))):
        print(i)
        break