import numpy as np
from M_dmp_main import sendcoords as DMP_T

class Traj:
    def __init__(self, NOC=100):
        self.no_of_cord = NOC

    def genrandCvector(self):
        vector = np.zeros((1, 3))
        for i in range(self.no_of_cord):
            random_points = (np.random.rand(3) + np.array([-0.5, -0.5, 0.5])) * np.array([1, 1, 0.5])
            vector = np.vstack((vector, random_points))
        vector = np.delete(vector, 0, 0)
        print('genrand',vector)
        return vector

    def mainVec(self):
        vector = np.zeros((1, 3))
        a = DMP_T()
        for i in range(self.no_of_cord):
            mainPoints = (a[:, i] + np.array([-0.5, -0.5, 0.5])) * np.array([1, 1, 0.5])
            vector = np.vstack((vector, mainPoints))
        vector = np.delete(vector, 0, 0)
        print(vector)
        return vector
