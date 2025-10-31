# TODO: Validate Expression

INVALID_ENDINGS = ["^", "+", "-", "*", "/", ".", "("]
OPERATORS_AND_OPEN_PARENTHESIS = ["^", "+", "-", "*", "/", "("]
OPERATORS = ["^", "+", "-", "*", "/"]

def is_valid_expression(expression: str):
    if not expression:
        return False
    
    if expression[-1] in INVALID_ENDINGS or expression[0] in OPERATORS:
        return False
    
    operator_present = False
    parenthesis_stack = []
    for i in range(len(expression)):
        if expression[i] == "(":
            if ((i != 0 and expression[i - 1] not in OPERATORS_AND_OPEN_PARENTHESIS)
                or expression[i + 1] == ")"):
                print(1)
                return False
            
            parenthesis_stack.append(expression[i])

        elif expression[i] == ")":
            if parenthesis_stack:
                parenthesis_stack.pop()
            else:
                print(2)
                return False

        elif expression[i] in OPERATORS:
            if not expression[i + 1].isdigit() and expression[i + 1] != "(":
                print(3)
                return False
            
            operator_present = True

    if parenthesis_stack or not operator_present:
        print(4)
        return False
    
    return True