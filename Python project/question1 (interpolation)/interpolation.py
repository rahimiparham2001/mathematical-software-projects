import sympy as sp

x = sp.symbols('x')
xs = [1, 2, 3, 4, 5, 6]
ys = [1, 3, 5, 8, 5, 2]
n = len(xs) - 1

# -------- 1) Lagrange interpolation --------
P = 0
for i in range(len(xs)):
    Li = 1
    for j in range(len(xs)):
        if i != j:
            Li *= (x - xs[j]) / (xs[i] - xs[j])
    P += ys[i] * Li

P = sp.expand(P)
print("Lagrange polynomial:")
print(P)

# -------- 2) Natural cubic spline --------
# S_i(x) = a_i*x^3 + b_i*x^2 + c_i*x + d_i
a = sp.symbols(f'a0:{n}')
b = sp.symbols(f'b0:{n}')
c = sp.symbols(f'c0:{n}')
d = sp.symbols(f'd0:{n}')

eqs = []

for i in range(n):
    Si = a[i]*x**3 + b[i]*x**2 + c[i]*x + d[i]
    eqs.append(sp.Eq(Si.subs(x, xs[i]), ys[i]))
    eqs.append(sp.Eq(Si.subs(x, xs[i+1]), ys[i+1]))

for i in range(1, n):
    S_prev = a[i-1]*x**3 + b[i-1]*x**2 + c[i-1]*x + d[i-1]
    S_next = a[i]*x**3 + b[i]*x**2 + c[i]*x + d[i]

    eqs.append(sp.Eq(sp.diff(S_prev, x).subs(x, xs[i]),
                     sp.diff(S_next, x).subs(x, xs[i])))
    eqs.append(sp.Eq(sp.diff(S_prev, x, 2).subs(x, xs[i]),
                     sp.diff(S_next, x, 2).subs(x, xs[i])))

S0 = a[0]*x**3 + b[0]*x**2 + c[0]*x + d[0]
Sn = a[n-1]*x**3 + b[n-1]*x**2 + c[n-1]*x + d[n-1]
eqs.append(sp.Eq(sp.diff(S0, x, 2).subs(x, xs[0]), 0))
eqs.append(sp.Eq(sp.diff(Sn, x, 2).subs(x, xs[-1]), 0))

unknowns = list(a) + list(b) + list(c) + list(d)
sol = sp.solve(eqs, unknowns, dict=True)[0]

print("\nNatural cubic spline pieces:")
for i in range(n):
    Si = sp.expand((a[i]*x**3 + b[i]*x**2 + c[i]*x + d[i]).subs(sol))
    print(f"S_{i}(x) on [{xs[i]}, {xs[i+1]}] = {Si}")
