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
            curr_node = Node(operand=char, left=curr_numeric)
            left = curr_numeric
            curr_numeric = ""

        else:
            raise ValueError(f"invalid value: {char}")

    if curr_node:
        curr_node.right = curr_numeric

    else:
        raise ValueError("not enough expressions...")

    print(curr_node)

tokenize(test_expression)
