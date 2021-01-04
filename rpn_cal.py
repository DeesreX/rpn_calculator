def calcu(stack, item):
    res = int(stack[0])
    stack.pop(0)
    if item == '+':
        for i in stack:
            res += int(i)
    if item == '-':
        for i in stack:
            res -= int(i)
    if item == '*':
        for i in stack:
            res *= int(i)
    if item == '/':
        for i in stack:
            res /= int(i)
    stack.clear()
    stack.append(res)
    return stack

if __name__ == "__main__":
    operators=['+','-','*','/']
    stack=[]
    while True:
        user_i = input()
        if user_i.lower() == 'off': break
        if user_i.isdigit() and user_i not in operators:
            stack.append(user_i)
        if user_i in operators:
            stack = calcu(stack, user_i)
            print(stack[0])