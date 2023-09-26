import numpy as np
import matplotlib.pyplot as plt
from numba import njit, prange
string_for_fractals = "ABBBAA"
N = 100
@njit
def r_n(ch_ : str
        , a : float
        , b : float
        ) -> float:
    if(ch_ == 'A'):
        return a
    if(ch_ != 'B'):
        print('Error')
        return 0
    return b



x = np.linspace(2,4,501)
y = np.linspace(2,4,501)
X, Y = np.meshgrid(x, y)

@njit()
def Lyapunov_fractal_initial(
       nx: int = 200,
       ny: int = 200,
):
    # Created list to store all log(|r_n * (1 - x_n)|) and then summarize it
    arr = np.zeros((nx + 1, ny + 1))
    len_of_string = 6
    a0 = 2
    a1 = 4
    b0 = 2
    b1 = 4
    for i in range(0, nx + 1):
        dx = (a1 - a0) / (nx)
        a = a0 + dx * i
        for j in range(0, ny + 1):
            dy = (b1 - b0) / ny
            b = b0 + dy * j
            sm = 0
            x_current = 0.5
            for n in range(0, N):
                for m in range(0, len_of_string):
                    r_n_ = r_n(string_for_fractals[m], a, b)
                    x_current = r_n_ * x_current * (1 - x_current)
                    tmp = np.abs(r_n_ * (1 - 2 * x_current))
                    if 0 < tmp:
                        sm = sm + np.log(tmp)
            if sm > 0:
                arr[j, i] = 1.333
            else:
                arr[j, i] = 0.333
    return arr
arr = Lyapunov_fractal_initial(500, 500)
plt.xlim(2, 4)
plt.ylim(2, 4)
plt.pcolor(X, Y, arr, cmap=plt.cm.Spectral)
plt.colorbar()
plt.show()

