import math


def normalize():
    # zwraca na wyjście sygnał z wejścia czyli sumę ważoną
    return lambda x: x


def line():
    return lambda x, a=1, b=0: a*x + b


def line_a():
    return lambda x, y=0, b=0: (y - b)/x


def line_b():
    return lambda x, y=0, a=1: y - a*x


def sigmoid():
    # return lambda x: 1 / (1 + pow(math.e, -x))
    return lambda x: 1 / (1 + math.exp(-x))


def bipolar_sigmoid():
    # return lambda x: 1 / (1 + pow(math.e, -x))
    return lambda x: (2 / (1 + math.exp(-x))) - 1


def binary_step():
    return lambda x, threshold=0: 1 if x > threshold else 0


def tangens_hiperbolic():
    return lambda x: math.tanh(x)


def sqnl():
    # unlinear squere
    return lambda x: x / abs(x) if x > 2 or x < -2 else x-(x**2/4)*((x+x+1) / abs((x+x+1)))


def arctan():
    return lambda x: math.atan(x)


def arsinh():
    return lambda x: math.asinh(x)


def softsign():
    return lambda x: x / (abs(x) + 1)


def isru():
    return lambda x, a=1: x / math.sqrt(1 + a*(x**2))


def isrlu():
    return lambda x, a=1: x / math.sqrt(1 + a*(x**2)) if x < 0 else x


def plu():
    return lambda x, a=0.1, b=1: max((a*(x+b)-b, min(a*(x-b)+b), x))


def relu():
    return lambda x, threshold=0: x if x > threshold else 0


def brelu():
    return lambda x, i: relu()(x) if i % 2 == 0 else -relu()(-x)


def prelu():
    # default leaky relu
    return lambda x, a=0.01: a*x if x < 0 else x


def gelu():
    return lambda x: x*(1 + math.erf(x/math.sqrt(2)))/2


def elu():
    return lambda x, a=1: x if x > 0 else a*(math.e**x - 1)


def selu():
    return lambda x: 1.507*x if x >= 0 else 1.507*(1.67326*(math.e**x - 1))


def softplus():
    return lambda x: math.log(1 + math.e**x)


def bent_identity():
    return lambda x: (math.sqrt(x**2 + 1) - 1)/2 + x


def _soft_exponential_no_0(a):
    return lambda x: ((math.e**(a*x)) - 1)/a + a if a > 0 else -((math.log(1 - a*(x+a)))/a)


def soft_exponential():
    return lambda x, a: x if a == 0 else _soft_exponential_no_0(a)(x)


def soft_clipping():
    return lambda x, a: (1/a)*math.log((1+math.e**(a*x))/(1+math.e**(a*(x-1))))


def sinusoid():
    return lambda x: math.sin(x)


def sinc():
    return lambda x: 1 if x == 0 else math.sin(x)/x


def gaussian():
    return lambda x: math.e**(-x**2)


def _sq_rbf_threshold():
    return lambda x: 1 - (x**2)/2 if abs(x) <= 1 else ((2-abs(x))**2)/2


def sq_rbf():
    return lambda x: 0 if abs(x) >= 2 else _sq_rbf_threshold()(x)


def derivative(fn, *attr):
    return lambda x, x0=0: (fn()(x0 + (x - x0), *attr) - fn()(x0, *attr)) / (x - x0)

def complex_derivative(fn1, fn2, deriv_fn2, *fn1_args):
    return lambda x, x0=0,*args: derivative(fn1, *fn1_args)(fn2(x, *args))*deriv_fn2(x, x0)