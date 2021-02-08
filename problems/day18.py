from problems.common import get_input_of_day
import re
from functools import reduce


def split_into_tokens(s):
    token_list = re.split('([0-9]+|[()])', re.sub(r'\s+','',s))
    return [x for x in token_list if x != '']


def add_or_multiply(a, b, op):
    if op == '*':
        return a * b
    return a + b


def evaluate_expression(tokens):
    result_stack = [0]
    op_stack = ['+']
    for token in tokens:
        if token.isnumeric():
            result_stack[0] = add_or_multiply(result_stack[0], int(token), op_stack[0])
        elif token in ('+', '*'):
            op_stack[0] = token
        elif token == '(':
            result_stack = [0] + result_stack
            op_stack = ['+'] + op_stack
        else:
            first = result_stack[0]
            op_stack = op_stack[1:]
            result_stack = result_stack[1:]
            result_stack[0] = add_or_multiply(result_stack[0], first, op_stack[0])
    return result_stack[0]


def evaluate_expression_weird(tokens):
    def helper(tokens):
        result_stack = [0]
        op_stack = ['+']
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == ')':
                return reduce(lambda x, y: x * y, result_stack), i
            elif token.isnumeric():
                if op_stack[0] == '+':
                    result_stack[0] += int(token)
                else:
                    result_stack = [int(token)] + result_stack
            elif token in ('+', '*'):
                op_stack[0] = token
            elif token == '(':
                paren, incr = helper(tokens[i + 1:])
                if op_stack[0] == '+':
                    result_stack[0] += paren
                else:
                    result_stack = [paren] + result_stack
                i += incr + 1
            else:
                raise ValueError('Unknown Token')
            i += 1
        return reduce(lambda x, y: x * y, result_stack), i

    result, _ = helper(tokens)
    return result


def process_input(input_list):
    expressions = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            expressions.append(clean)
    return expressions


def solve_part1(input_list):
    expressions = process_input(input_list)
    token_lists = list(map(split_into_tokens, expressions))
    return sum(list(map(evaluate_expression, token_lists)))


def solve_part2(input_list):
    expressions = process_input(input_list)
    token_lists = list(map(split_into_tokens, expressions))
    return sum(list(map(evaluate_expression_weird, token_lists)))


if __name__ != 'main':
    print(solve_part1(get_input_of_day(18)))
    print(solve_part2(get_input_of_day(18)))
