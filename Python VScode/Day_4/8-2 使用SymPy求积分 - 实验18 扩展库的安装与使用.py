import sympy
x = sympy.Symbol("x")
g = sympy.exp(-x**2)
print(sympy.integrate(g, (x, -sympy.oo, 0)))
print("严浩睿20240395")