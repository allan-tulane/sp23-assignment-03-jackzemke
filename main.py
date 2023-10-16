# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

#### Iterative solution
def parens_update(current_output, next_input):
    # print(current_output)
    # print(next_input)
    c = current_output
    if next_input == '(':
        c += 1
    if next_input == ')':
        c += -1
    if c < 0:
        c += -math.inf
    return c

def parens_match_iterative(mylist):
    c = 0
    return iterate(parens_update,parens_update(c,mylist),mylist) == 0

def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(','a', ')', ')', 'b', '(']) == False
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True

test_parens_match_iterative()

#### Scan solution


def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def plus(x,y):
    return x+y

def parens_match_scan(mylist):
    mylist = list(map(paren_map,mylist))
    # print(mylist)
    a = scan(plus,0,mylist)
    b = reduce(min_f,0,a[0])
    # print(b)
    # a = reduce(lambda x,y: x+y, 0)
    # print(a)
    if a[1] != 0 or b != 0:
        return False
    else:
        return True
    


def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(','a', ')', ')', 'b', '(']) == False
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True

# print(parens_match_scan(['(', ')']))
# print(parens_match_scan(['(']))
# print()
# print(parens_match_scan(['(','a', ')', ')', 'b', '(']))
# print()
# print(parens_match_scan(['(']))

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    

    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    ###TODO
    pass
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
