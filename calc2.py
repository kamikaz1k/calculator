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

OPERATORS = {"*","+","-","/"}


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

    while i < length:

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
            raise ValueError("expression did not start with a number..." + char)

        while char.isnumeric():
            curr_buffer += char
            i += 1

            if i >= length:
                break

            char = expr[i]

        curr_node = Node(operand=operand, left=last_number, right=int(curr_buffer))
        curr_buffer = ""

        if not root:
            root = curr_node

    return root

print(parse("1 + 1"))

print(parse("1 * 2"))

print(parse("1 / 3"))

print(parse("1 - 4"))
