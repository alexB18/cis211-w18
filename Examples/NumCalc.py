ops = {"+": lambda x, y: x + y,
       "-": lambda x, y: x - y,
       "*": lambda x, y: x * y,
       "/": lambda x, y: x // y,}

def eval_postfix(s: str) -> int:
    """Input should look like "5 3 + 4 *"
    Example: eval_postfix("5 3 + 4 *") -> 32
    """


    stack = []
    tokens = s.split()
    for i in tokens:
        if i.isnumeric():
            stack.append(int(i))
        elif i in ops:
            right = stack.pop()
            left = stack.pop()
            result = ops[i](left, right)
            stack.append(result)

    return stack[0]


def parse_postfix(s: str) -> list:
    """Input should look like "5 3 + 4 *"
    Example: eval_postfix("5 3 + 4 *") -> 32
    """
    
    stack = []
    tokens = s.split()
    for i in tokens:
        if i.isnumeric():
            stack.append(int(i))
        elif i in ops:
            right = stack.pop()
            left = stack.pop()
            result = [i, left, right]
            stack.append(result)

    return stack[0]

def eval_sexp(sexp: list) -> int:
    if isinstance(sexp, int):
        return sexp
    else:
        right = eval_sexp(sexp.pop())
        left = eval_sexp(sexp.pop())
        op = sexp.pop()

        return  ops[op](left, right)


print(parse_postfix("5 3 - 4 *"))


