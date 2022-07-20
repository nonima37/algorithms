PREC = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
ASSOC = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

def get_next_token(s):
    tokens = s.split(' ')
    for t in tokens:
        yield t

def compare(t1, t2):
    if t2 == '(':
        return True

    if (PREC[t1] > PREC[t2] or PREC[t1] == PREC[t2] and ASSOC[t1] == 'right'):
        return True
    else:
        return False

def process(token, stack):
    retval = ''

    # pushing stuff to the stack whenever 
    # lower precendence is encountered, current stack is added to the output
    if stack:
        # if paren is closed add operators to output cuz whatevers nex is lower 
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                retval += stack.pop() + ' '
            stack.pop()
        elif compare(token, stack[-1]):
            stack.append(token)
        else:
            while not compare(token, stack[-1]):
                retval += stack.pop() + ' '
                if not stack:
                    break
            stack.append(token)
    else:
        stack.append(token)

    return retval

def convert(input):
    stack = []
    output = ''
    for token in get_next_token(input):
        try:
            int(token)
        except ValueError:
            output += process(token, stack)
        else:
            output += token + ' '

    while stack:
        output += stack.pop() + ' '
    return output

def calc(input):
    postfix = convert(input).replace(' ', '')
    expr = []

    for i in range(len(postfix)):
        try:
            expr.append(int(postfix[i]))
        except ValueError:
            if postfix[i] == "+":
                expr[0] += expr[1]
            elif postfix[i] == "-":
                expr[0] -= expr[1]
            elif postfix[i] == "*":
                expr[0] *= expr[1]
            elif postfix[i] == "/":
                expr[0] /= expr[1]

            del expr[1]
    print(expr)

calc("2 * 2 / 3")
