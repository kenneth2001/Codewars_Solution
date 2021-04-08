import numpy as np
def fib(n):
    if n >= 0:
        a = np.array([[0,1],[1,1]], object)
    else:
        a = np.array([[-1,1],[1,0]], object)
    b = np.array([[0],[1]])
    return np.matmul(np.linalg.matrix_power(a, abs(n)), b)[0][0]
