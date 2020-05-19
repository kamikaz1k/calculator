OPERATORS = {"*","+","-","/"}

test_expression = "1 * 10"


class Node:
    def __init__(self, operand, left=None, right=None):
        self.operand = operand
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<Node operand=`{self.operand}` left=`{self.left}` right=`{self.right}` />"

    __str__ = __repr__


def tokenize(expr):
    root = None

    left = None
    operand = None
    right = None

    curr_numeric = ""
    curr_node = None

    for char in expr:
        if char.isnumeric():
            curr_numeric += char

        elif char == " ":
            continue

        elif char in OPERATORS:
            left = int(curr_numeric)
            curr_node = Node(operand=char, left=left)
            curr_numeric = ""

        else:
            raise ValueError(f"invalid value: {char}")

    if curr_node:
        curr_node.right = int(curr_numeric)
        curr_numeric = ""

    else:
        raise ValueError("not enough expressions...")

    print(curr_node)
    return curr_node

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

ast = tokenize(test_expression)

print(test_expression, " = ", evaluate(ast))
