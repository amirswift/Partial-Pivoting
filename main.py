import numpy as np
from scipy.interpolate import CubicSpline



n=1000




C = np.loadtxt("sample.txt")
C=C[0:n][0:n]
A=[]

for i in range(n):
    A.append(C[i][:n])

A=np.array(A)
print(A.shape)
n, _ = A.shape

b = np.array([(i+2)/(2*i+1) for i in range(n)], dtype=float)


def lu_decomposition_pp(A):
    n = A.shape[0]
    U = A.copy().astype(float)
    L = np.eye(n)
    P = np.eye(n)

    for k in range(n):
        # Partial pivot
        pivot = np.argmax(np.abs(U[k:, k])) + k
        if pivot != k:
            U[[k, pivot]] = U[[pivot, k]]
            P[[k, pivot]] = P[[pivot, k]]
            if k > 0:
                L[[k, pivot], :k] = L[[pivot, k], :k]

        for i in range(k+1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return P, L, U

P, L, U = lu_decomposition_pp(A)


Pb = P @ b
y = np.zeros(n)
for i in range(n):
    y[i] = Pb[i] - np.sum(L[i,:i]*y[:i])


x = np.zeros(n)
for i in reversed(range(n)):
    x[i] = (y[i] - np.sum(U[i,i+1:]*x[i+1:])) / U[i,i]

print(f"Solution x for {n}x{n} system:")
print(x)


def count_ops_pp(A_sub, b_sub):
    n = A_sub.shape[0]
    ops = 0
    A = A_sub.copy()
    b = b_sub.copy()

    for k in range(n):
        pivot = np.argmax(np.abs(A[k:, k])) + k
        if pivot != k:
            A[[k,pivot]] = A[[pivot,k]]
            b[[k,pivot]] = b[[pivot,k]]
        for i in range(n):
            if i != k:
                factor = A[i,k]/A[k,k]

                ops += n - k

                ops += 1
                A[i,k:] -= factor * A[k,k:]
                b[i] -= factor * b[k]
    return ops


sub_ns = [1,5,10,12,15,18,20,25,28,29,50]
ops_list = []

for i in sub_ns:
    subA = A[:i,:i]
    subb = b[:i]
    ops = count_ops_pp(subA, subb)
    ops_list.append(ops)

print("Submatrix sizes:", sub_ns)
print("Operations per size:", ops_list)



ops_array = np.array(ops_list, dtype=float) 

def newton_divided_diff(x, y):
    i = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1,i):
        coef[j:i] = (coef[j:i] - coef[j-1:i-1]) / (np.array(x[j:i]) - x[j-1])
    return coef

def newton_eval(coef, x_data, x):
    k = len(coef)
    result = coef[-1]
    for i in range(k-2, -1, -1):
        result = result*(x - x_data[i]) + coef[i]
    return result

coef = newton_divided_diff(sub_ns, ops_array)
ops_N_newton = newton_eval(coef, sub_ns, n)
print(f"Estimated operations for n={n} (Newton):", ops_N_newton)

cs = CubicSpline(sub_ns, ops_array)
ops_N_spline = cs(n)
print(f"Estimated operations for n={n} (Cubic Spline):", ops_N_spline)


