from operator import add, sub, mul, truediv

OP_DICT = {
    'plus': add,
    'minus': sub,
    'multiplied': mul,
    'divided': truediv
}


def is_digit(num_str: str) -> bool:
    return (
        num_str.isdigit() or
        # If the number happens to be negative, we need to remove - sign first
        num_str[1:].isdigit()
    )
  
  
def has_digits(text: str) -> bool:
    return any(token.isdigit() for token in text)
  
  
def get_expr(question: str) -> str:
    math_expr = (
        question[8:-1]        # Remove the 'What is ' and '?''
        .replace('by', '')    # Remove 'by' so that all op. descs. are 1 token only
        .split()
    )
    if not math_expr:
        # Math expression is empty
        raise ValueError('syntax error')
        
    if not has_digits(question):
        # The question must contain at least 1 number to be considered a "math question"
        raise ValueError('unknown operation')
        
    if not is_digit(math_expr[0]):
        raise ValueError('syntax error')
        
    return math_expr
  
  
def get_result(math_expr: str) -> int:
    res = int(math_expr[0])
    token_n = len(math_expr)
    
    for i in range(1, token_n, 2):
        op_desc = math_expr[i]
        if op_desc.isdigit():
            raise ValueError('syntax error')
            
        op_func = OP_DICT.get(op_desc)
        if op_func is None:
            # The operation is neither add, sub., mul., or div.
            raise ValueError('unknown operation')
            
        operand_idx = i + 1
        if operand_idx == token_n:
			# the operand is not in the expression
            raise ValueError('syntax error')
            
        operand = math_expr[operand_idx]
        if not is_digit(operand):
            # the operand is not a number
            raise ValueError('syntax error')
            
        res = op_func(res, int(operand))
    return res
    
    
def answer(question: str) -> int:
    math_expr = get_expr(question)
    return get_result(math_expr)
