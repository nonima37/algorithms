import re

class Num:
    def __init__(self, val):
        self.value = float(val) if '.' in val else int(val)
    def __repr__(self):
        return f'Num: {self.value}'

def lexan(input_string):
    i = 0
    while i < len(input_string):
        c = input_string[i]
        if c.isdigit() or c == '.':
            val = re.match(r'[.0-9]+', input_string[i:])[0]
            yield Num(val)
            i += len(val)
        else:
            if input_string[i:i + 2] == '**':
                yield '**'
                i += 1
            elif c != ' ':
                yield c
            i += 1

# addition and subtraction
def expr():
    result = term()
    while True:
        if look_ahead == '+':
            match('+')
            result += term()
        elif look_ahead == '-':
            match('-')
            result -= term()
        else:
            break
    return result
    
# subtraction and multiplication
def term():
    result = factor()
    while True:
        if look_ahead == '*':
            match('*')
            result *= factor()
        elif look_ahead == '/':
            match('/')
            result /= factor()
        else:
            break

    return result

# power operation
def factor():
    result = base()
    if look_ahead == '**':
        match('**')
        result **= factor()
    return result

# executes if there's a parantheses or just returns a number
def base():
    if look_ahead == '(':
        match('(')
        result = expr()
        match(')')
    elif isinstance(look_ahead, Num):
        result = look_ahead.value
        match(look_ahead)
    # if the first number is negative
    elif look_ahead == '-':
        match('-')
        result = -1 * base()
    else:
        match('number')
    return result

def match(t):
    global look_ahead

    # i don't think these are needed 
    #if t == look_ahead:
    try:
        look_ahead = next(token_gen)
    except StopIteration:
        look_ahead = ''
    #else:
    #    raise RuntimeError(f'Malformed input. Token {look_ahead}')

def main(input_string):
    global token_gen, look_ahead
    token_gen = lexan(input_string)
    look_ahead = next(token_gen)
    result = expr()
    #match('') #?
    return result

print(main(2+3*(3/2-4)))
# each function is performing specific operations but before they do,
# they call other functions that perform higher precendence operations,
# and add(or whatever operationg) that result to the result variable
# look_ahead variable is being pushed by one element along the way
