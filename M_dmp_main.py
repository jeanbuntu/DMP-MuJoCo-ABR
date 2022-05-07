import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from M_DMP_Class import DMP
from settraj import inputT

traj = inputT()

xpts = traj[0]
ypts = traj[1]
zpts = traj[2]

n = xpts.shape[0]
dt = 1e-2
T = n * dt
a = 10
b = a / 4
n_bfs =500
iter_no = 1

dmpX = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmpX.fit(xpts)

dmpY = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmpY.fit(ypts)

dmpZ = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmpZ.fit(zpts)

xp = np.zeros(dmpX.cs.N)
yp = np.zeros(dmpY.cs.N)
zp = np.zeros(dmpY.cs.N)

k = 1.1
for i in range(dmpX.cs.N):
    # print(i)
    xp[i], _, _, _, A_Gx = dmpX.step(k=k, actuate=0)
    yp[i], _, _, _, A_Gy = dmpY.step(k=k, actuate=0)
    zp[i], _, _, _, A_Gz = dmpZ.step(k=k, actuate=0)

#
# # plt.figure(figsize=(6, 6))
# fig = plt.figure()
# Axes3D(fig)
#
# Axes3D.plot(xpts, ypts, zpts, label="Reference trajectory")
# Axes3D.plot(xp, yp, zp, label="DMP trajectory")
# # plt.plot(A_Gx, A_Gy, 'o', label='Actual Goal')
# # plt.plot(xp[-1], yp[-1], 'o', label='DMP updated Goal')
# # plt.legend()
# plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')

plt.plot(xp, yp, zp, c='g', label='Remapped goal trajectory')
plt.plot(xpts, ypts, zpts, c='r', label='Original Trajectory')
plt.legend()
plt.show()
print('DMP done')


def sendcoords():
    print('sending coordinates to Mujoco')
    return np.array([xp, yp, zp])
