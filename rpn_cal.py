

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

def cal(exp):
    exp_list = []
    for item in exp.split(' '): exp_list.append(item)

    operators = ['+', '-', '*', '/']
    
    stack = []
    for item in exp_list:
        if not item in operators:
            stack.append(item)
        if item in operators:
            stack = calcu(stack, item)
    return stack[0]



if __name__ == "__main__":


    print(cal(input()))