PREC = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
ASSOC = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

def compare(t1, t2):
    if t2 == '(':
        return True

    if (PREC[t1] > PREC[t2] or PREC[t1] == PREC[t2] and ASSOC[t1] == 'right'):
        return True
    else:
        return False

def process(token, stack, output):
    #retval = []
    # pushing stuff to the stack whenever 
    # lower precendence is encountered, current stack is added to the output
    if stack:
        # if paren is closed add operators to output cuz whatevers nex is lower 
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif compare(token, stack[-1]):
            stack.append(token)
        else:
            while not compare(token, stack[-1]):
                output.append(stack.pop())
                if not stack:
                    break
            stack.append(token)
    else:
        stack.append(token)

def convert(input_string):
    stack = []
    output = []
    for token in input_string.split(' '):
        try:
            int(token)
        except ValueError:
            process(token, stack, output)
        else:
            output.append(token)

    while stack:
        output.append(stack.pop())
    return output

def calc(input_string):
    postfix = convert(input_string)
    expr = []
    cur_index = len(expr) - 1
    print(postfix)
    for i in range(len(postfix)):
        try:
            expr.append(int(postfix[i]))
        except ValueError:
            if postfix[i] == "+":
                expr[len(expr)-2] += expr[len(expr)-1]
            elif postfix[i] == "-":
                expr[len(expr)-2] -= expr[len(expr)-1]
            elif postfix[i] == "*":
               expr[len(expr)-2] *= expr[len(expr)-1]
            elif postfix[i] == "/":
               expr[len(expr)-2] /= expr[len(expr)-1]
            del expr[-1]
    print(expr)

calc("2 - 1 * ( 8 - 2 ) / 2")




