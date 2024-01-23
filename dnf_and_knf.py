from sympy.logic.boolalg import to_dnf, to_cnf
from sympy.abc import A, B, C
"""
Sympy shenanigangs:

& (And)
| (Or)
~ (Not)

and implications:
x >> y
Implies(x, y)
x << y
Implies(y, x)
"""

boolean_formula= (A | B) >> C


dnf = to_dnf(boolean_formula)
cnf = to_cnf(boolean_formula)
print("disjunktive normalform:", dnf) #dnf
print("konjuktive normalform:", cnf) #knf