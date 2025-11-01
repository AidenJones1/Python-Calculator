from .nodes import OperatorNode, NumberNode

def is_valid_expression(expression: str) -> bool:
    INVALID_ENDINGS = set(["^", "+", "-", "*", "/", ".", "("])
    OPERATORS_AND_OPEN_PARENTHESIS = set(["^", "+", "-", "*", "/", "("])
    OPERATORS = set(["^", "+", "-", "*", "/"])

    if not expression: # Empty string
        return False
    
    if expression[-1] in INVALID_ENDINGS or expression[0] in OPERATORS: # e.g. '-4' OR '4-' OR '7.'
        return False
    
    operator_present = False
    parenthesis_stack = []
    for i in range(len(expression)):
        if expression[i] == "(":
            if ((i != 0 and expression[i - 1] not in OPERATORS_AND_OPEN_PARENTHESIS) # e.g. '9(5+6)'
                or expression[i + 1] in OPERATORS or expression[i + 1] == ")"):  # e.g. '()'
                return False
            
            parenthesis_stack.append(expression[i])

        elif expression[i] == ")":
            if parenthesis_stack:
                parenthesis_stack.pop()

            else: # e.g. '(5+3))'
                return False

        elif expression[i] in OPERATORS:
            if not expression[i + 1].isdigit() and expression[i + 1] != "(": # e.g. '9+*' OR '4-)'
                return False
            
            operator_present = True

    # e.g. '((5+3)'
    if parenthesis_stack or not operator_present:
        return False
    
    return True

def shunting_yard_algorithm(expression: str) -> list[str]:
    OPERATORS = set(["^", "+", "-", "*", "/"])
    PRECEDENCE = {"^" : 3, "*" : 2, "/" : 2, "+" : 1, "-" : 1}
    ASSOCIATIVITY = {"^" : "R", "*" : "L", "/" : "L", "+" : "L", "-" : "L"}

    output_queue: list[str] = []
    op_stack = []

    while len(expression) > 0:
        token = expression[0]

        if token.isdigit():
            # Look ahead for consecutive numbers
            j = 1
            while j < len(expression) and expression[j].isdigit():
                token += expression[j]
                j += 1
        
            # Jump to next non-number
            expression = expression[j:]

            # Add number to output queue
            output_queue.append(token)
            continue

        elif token in OPERATORS:
            while (op_stack and op_stack[-1] in OPERATORS and
                   ((ASSOCIATIVITY[token] == "L" and PRECEDENCE[token] <= PRECEDENCE[op_stack[-1]]) or 
                   (ASSOCIATIVITY[token] == "R" and PRECEDENCE[token] < PRECEDENCE[op_stack[-1]]))):
                output_queue.append(op_stack.pop())
            op_stack.append(token)

        elif token == "(":
            op_stack.append(token)

        elif token == ")":
            # Push operations within the parenthesis to the queue
            while op_stack and op_stack[-1] != "(":
                output_queue.append(op_stack.pop())

            # Remove '(' from the stack
            op_stack.pop()

        # Iterate to next character
        expression = expression[1:]

    # Push remaining operations onto the queue
    while op_stack:
        output_queue.append(op_stack.pop())

    return output_queue

def convert_to_tree(postfix_expression: list[str]) -> OperatorNode:
    OPERATORS = set(["^", "+", "-", "*", "/"])

    stack = []
    for token in postfix_expression:
        if token.isdigit():
            num_node = NumberNode(value = token)
            stack.append(num_node)

        elif token in OPERATORS:
            r_node = stack.pop()
            l_node = stack.pop()

            op_node = OperatorNode(value = token, right_node = r_node, left_node = l_node)
            stack.append(op_node)
    
    root = stack.pop()
    return root