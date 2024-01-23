import ttg

"""Truth table generation using ttg module"""
"""generation using 0 and 1"""
#print(ttg.Truths(['p', 'q', 'r'], ['p and q and r', 'p or q or r', '(p or (~q)) => r']))
"""generation using True and False"""
#print(ttg.Truths(['p', 'q'], ['p and q', 'p or q', '(p or (~q)) => (~p)'], ints=False))
"""
Truth table shenanigans:
    negation: 'not', '-', '~'
    logical disjunction: 'or'
    logical nor: 'nor'
    exclusive disjunction: 'xor', '!='
    logical conjunction: 'and'
    logical NAND: 'nand'
    material implication: '=>', 'implies'
    logical biconditional: '='
"""

print(ttg.Truths(['A','B','C'], ['A or B','(A or B) => C']))


