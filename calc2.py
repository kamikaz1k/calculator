# "1 + 1"

# + 1 1



# 1 + 1 * 3

#     +
#   1   *
#     1   3



# scan the first number

# store it as last_number

# ignore spaces

# expect operand

# ignore spaces

# scan for next number

# make node with operand and values

# ignore spaces

# scan for operand

# ignore spaces

# scan for next number

MULT = "*"
DIV = "/"

OPERATORS = {MULT, DIV, "+", "-"}


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
            if operand in (MULT, DIV):
                # if priority operand, ensure it is inserted below
                tmp = Node(operand=operand, left=curr_node.right, right=int(curr_buffer))
                curr_node.right = tmp

            else:
                curr_node = Node(operand=operand, left=curr_node, right=int(curr_buffer))



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

    return val

def parse_and_eval(expr):
    ast = parse(expr)
    # print("AST", ast)
    result = evaluate(ast)
    print(expr, " = ", result, f"| eval ({eval(expr) == result}):", eval(expr))

parse_and_eval("1 + 1")

parse_and_eval("1 * 2")

parse_and_eval("1 / 3")

parse_and_eval("1 - 4")

parse_and_eval("1 - 4 + 1")

parse_and_eval("1 - 4 + 1 * 4")

parse_and_eval("1 * 4 + 1 * 4 + 5 * 2")
