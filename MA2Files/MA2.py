"""
Solutions to module 2 - A calculator
Student: Hugo Vennergrund Blom
Mail: hugo.vennergrundblom@student.uu.se
Reviewed by: Behnam
Reviewed date: 2024-09-17
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper

'''
    while wtok.get_current() == 'sin': 
        wtok.next()
        result = math.sin(factor(wtok, variables))

    while wtok.get_current() == 'cos': 
        wtok.next()
        result = math.cos(factor(wtok, variables))

    while wtok.get_current() == 'fac': 
        wtok.next()
        result = math.factorial(factor(wtok, variables))

    while wtok.get_current() == 'max': 
        wtok.next()
        result = max(factor(wtok, variables))
'''


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def log(x):
    if x <= 0:
        raise EvaluationError("Argument to log less than or equal to 0")
    return math.log(x)
def fac(x):
    if not x.is_integer():
        raise EvaluationError("Incorrect type of argument (e.g. fac(2.5))")
    if x < 0:
        raise ValueError("Fac can't have negative number")
    return math.factorial(int(x))

FUNCTIONS_1 = {'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': log, 'fac': fac}
FUNCTION_N = {'sum': sum, 'max': max}


def arglist(wtok, variables):
    arglist = []

    if wtok.get_current() != '(':
        raise SyntaxError("Arglist must start with '('")

    wtok.next()
    arglist.append(assignment(wtok, variables))

    while wtok.get_current() == ',':
        wtok.next()
        arglist.append(assignment(wtok, variables))

    if wtok.get_current() != ')':
        raise SyntaxError("Arglist incorrectly formated")

    return arglist


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if not wtok.is_at_end() and not wtok.get_current() == ')':
        raise SyntaxError('Incorrect line ending')
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)

    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = float(result)
        else:
            raise SyntaxError("Expected variable after '='")
        wtok.next()

        if not wtok.is_at_end() and (wtok.get_current() != ')' and wtok.get_current() != '='):
            raise SyntaxError("Can't follow variable assignment with expression")

    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()
        if wtok.get_previous() == '+':
            result = result + term(wtok, variables)
        else:
            result = result - term(wtok, variables)
        
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)

    while wtok.get_current() == '*' or wtok.get_current() == '/':# or wtok.get_current() == '**': 
        wtok.next()
        if wtok.get_previous() == '*':
            result = result * factor(wtok, variables)
        elif wtok.get_previous() == '/':
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError as _:
                raise EvaluationError("Division by 0")
        elif wtok.get_previous() == '**':
            result = math.pow(result, factor(wtok, variables))

    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise TokenError("Expected ')'")
        else:
            wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.is_name():
        if wtok.get_current() in FUNCTIONS_1:
            func = wtok.get_current()
            wtok.next()
            if wtok.get_current() != '(':
                raise SyntaxError("Arglist must start with '('")
            result = factor(wtok, variables)

            result = FUNCTIONS_1[func](result)

        elif wtok.get_current() in FUNCTION_N:
            func = wtok.get_current()
            wtok.next()
            result = FUNCTION_N[func](arglist(wtok, variables))

        elif wtok.get_current() in variables:
            result = float(variables[wtok.get_current()])
            wtok.next()
        else:
            raise EvaluationError(
                f'Undefined variable: {wtok.get_current()}')

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)
    elif wtok.get_current() == '+':
        wtok.next()
        result = factor(wtok, variables)
    else:
        raise SyntaxError(
            "Expected number or '('")  
    return result



def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#' or line == 'vars':
            if line == 'vars':
                print(variables)
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print('*** Evaluation Error. ', ee)




if __name__ == "__main__":
    main()
