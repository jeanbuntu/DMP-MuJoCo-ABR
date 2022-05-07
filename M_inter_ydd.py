import numpy as np
from scipy import interpolate


def interpolate_path(dmp, path):
    time = np.linspace(0, dmp.cs.T, path.shape[0])
    inter = interpolate.interp1d(time, path)
    y = np.array([inter(i * dmp.dt) for i in range(dmp.cs.N)])
    return y


def calc_derivatives(y, dt):
    yd = np.concatenate(([0], np.diff(y) / dt))  # gradient of position/time
    ydd = np.concatenate(([0], np.diff(yd) / dt))  # gradient of vel/time
    return yd, ydd
