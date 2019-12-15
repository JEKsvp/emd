import numpy as np


def getSignal(noise=.005):
    length = 250
    point_size = 2000
    t = np.linspace(0, length, point_size)

    nu, sigma = 0, noise
    s = np.random.normal(nu, sigma, point_size)

    x = np.linspace(-16*np.pi, 16*np.pi, point_size)
    x = x + s
    return [np.sin(x), t]
