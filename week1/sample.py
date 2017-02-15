
import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(0, 6, 0.1)
#y = np.sin(x)

#plt.plot(x, y)
#plt.show()

def AND_SIMPLE (x1, x2):
    w1, w2, theta = 0.2, 0.2, 0.3
    if x1 * w1 + x2 * w2 <= theta:
        return 0;
    else:
        return 1;


def AND (x1, x2):
    w1, w2, theta = 0.2, 0.2, 0.3
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = -1 * theta
    if np.sum(x * w) + b <= 0:
        return 0
    else:
        return 1

    
def NAND (x1, x2):
    w1, w2, theta = -0.2, -0.2, -0.3
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = -1 * theta
    if np.sum(x * w) + b <= 0:
        return 0
    else:
        return 1

def OR (x1, x2):
    w1, w2, theta = 0.2, 0.2, 0.1
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = -1 * theta
    if np.sum(x * w) + b <= 0:
        return 0
    else:
        return 1

def XOR (x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
