from Stack import Stack

def base_converter(dec, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while dec > 0:
        rem =  dec % base
        rem_stack.push(rem)
        dec = dec // base

    val = ""
    while not rem_stack.is_empty():
        val += digits[rem_stack.pop()]

    return val

print(base_converter(1010,16))
print(base_converter(25,2))
