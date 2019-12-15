from scipy.integrate import odeint
import numpy as np


def getSignal(noise=0.005):
    length = 250
    point_size = 2000
    mu = 0.5
    nu, sigma = 0, noise

    def vanderpol(X, t):
        x = X[0]
        y = X[1]
        dxdt = mu * (x - 1. / 3. * x ** 3 - y)
        dydt = x / mu
        return [dxdt, dydt]

    X0 = [0, 2]
    t = np.linspace(0, length, point_size)

    sol = odeint(vanderpol, X0, t)

    x = sol[:, 0]
    y = sol[:, 1]

    s = np.random.uniform(nu, sigma, point_size)
    x = x + s
    return [x, t]
