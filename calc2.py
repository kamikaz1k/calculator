EXP = "^"
MULT = "*"
DIV = "/"
ADD = "+"
SUB = "-"

OPERATORS = {EXP, MULT, DIV, ADD, SUB}


class Node:
    def __init__(self, operand, left=None, right=None):
        self.operand = operand
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<Node operand=`{self.operand}` left=`{self.left}` right=`{self.right}` />"

    __str__ = __repr__


def parse(expr):

    i = 0
    length = len(expr)
    root = None

    curr_node = None
    last_number = None
    operand = None
    curr_buffer = ""

    if i >= length:
        return root

    char = expr[i]

    while char == " ":
        i += 1
        if i >= length:
            return root

        char = expr[i]

    if not char.isnumeric():
        raise ValueError("expression did not start with a number... " + char)

    while char.isnumeric():
        curr_buffer += char
        i += 1

        if i >= length:
            raise Error("end of the line...")

        char = expr[i]

    last_number = int(curr_buffer)
    curr_buffer = ""

    while i < length:

        while char == " ":
            i += 1
            if i >= length:
                return root

            char = expr[i]

        if char not in OPERATORS:
            raise ValueError("not a valid operator: " + char)

        operand = char

        i += 1
        if i >= length:
            return root

        char = expr[i]

        while char == " ":
            i += 1
            if i >= length:
                return root

            char = expr[i]

        if not char.isnumeric():
            raise ValueError("expression did not end with a number..." + char)

        while char.isnumeric():
            curr_buffer += char
            i += 1

            if i >= length:
                break

            char = expr[i]

        if not curr_node:
            curr_node = Node(operand=operand, left=last_number, right=int(curr_buffer))

        else:
            if operand == EXP:
                # if exponent, it is highest priority so insert as leaf
                curr_node = Node(operand=operand, left=curr_node, right=int(curr_buffer))

            elif operand in (ADD, SUB):
                # if curr_node is add/sub, it is higher priority so insert as leaf
                if curr_node.operand == (ADD, SUB):
                    tmp = Node(operand=operand, left=curr_node.right, right=int(curr_buffer))
                    curr_node.right = tmp

                # otherwise insert as parent
                else:
                    curr_node = Node(operand=operand, left=curr_node, right=int(curr_buffer))

            else:
                # if curr_node is exp, it is lower priority so insert as parent
                if curr_node.operand == EXP:
                    curr_node = Node(operand=operand, left=curr_node, right=int(curr_buffer))

                # otherwise insert as leaf
                else:
                    tmp = Node(operand=operand, left=curr_node.right, right=int(curr_buffer))
                    curr_node.right = tmp


        curr_buffer = ""

        root = curr_node

    return root

def evaluate(root):

    left = root.left
    right = root.right

    if isinstance(left, Node):
        left = evaluate(left)

    operand = root.operand

    if isinstance(right, Node):
        right = evaluate(right)

    val = None

    if operand == "*":
        val = left * right

    elif operand == "+":
        val = left + right

    elif operand == "-":
        val = left - right

    elif operand == "/":
        val = left / right

    elif operand == EXP:
        val = left ** right

    return val


import time
def parse_and_eval(input_expr):

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    start = time.time()
    actual = parse(input_expr)
    actual = evaluate(actual)
    duration = time.time() - start
    duration = duration * 1_000_000

    expected_value = eval(input_expr.replace(EXP, "**"))
    result = actual == expected_value

    print("Result: ", OKGREEN if result else FAIL, result, ENDC, "time: {:7.3f} ns".format(duration), "Actual: ", actual, " Expected: ", expected_value, " Input: ", input_expr)

parse_and_eval("1 + 1")

parse_and_eval("1 * 2")

parse_and_eval("1 / 3")

parse_and_eval("1 - 4")

parse_and_eval("1 - 4 + 1")

parse_and_eval("1 - 4 + 1 * 4")

parse_and_eval("1 * 4 + 1 * 4 + 5 * 2")

parse_and_eval("2 ^ 3")
