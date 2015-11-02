from Stack import Stack

def parenCheck(string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False

print(parenCheck("((()))"))
print(parenCheck("((()"))
    
            
