def answer(x):
    orig = x
    while True:
        string = list(str(x))
        listVal = map(int,string)
        result = 0
        for i in range(0,len(listVal)):
            result += listVal[i]
        if result < 10:
            return result
        else:
            x = result

print(answer(1235))
