#!/usr/bin/env python3

def calculate(arg):
    stack = []

    tokens = arg.split()
    
    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '*':
                result = val1 * val2
            elif token == '/':
                if val2 == 0:
                    raise ValueError("Can't divide by 0")
                else:
                    result = val1 / val2
            elif token == '^':
                result = 1
                if val2 < 0:
                    val2 = val2 * -1
                    while val2 > 0:
                        result = val1 * result
                        val2 = val2 - 1
                    if result == 0:
                        raise ValueError("Can't divide by 0")
                    else:
                        result = 1 / result
                elif val2 > 0:
                    while val2 > 0:
                        result = val1 * result
                        val2 = val2 - 1
            stack.append(result)
    if len(stack) > 1:
        raise ValueError("Too many arguments on the stack")
    return stack[0]

def main():
    while True:
        try:
            result = calculate(input("rpn calc> "))
            print(result)
        except ValueError:
            pass

if __name__ == '__main__':
    main()
