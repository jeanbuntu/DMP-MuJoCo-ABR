import numpy as np

radius = 0.5
noofpoints = 100
x = np.linspace(-radius, radius * 0.99, int(noofpoints / 2))
x2 = np.linspace(radius, -radius * 0.99, int(noofpoints / 2))
y = radius * np.sqrt(1 - ((x / radius) ** 2))
y2 = radius * np.sqrt(1 - ((x2 / radius) ** 2))
x = np.append(x, x2)
y = np.append(y, y2)
t = np.linspace(-0.2, 0.75, noofpoints)
x += 0.5
y += 0.5
dataSet = np.array([x, y, t])
numDataPoints = len(t)


# fig = plt.figure()
# ax = Axes3D(fig)

# NOTE: Can't pass empty arrays into 3d version of plot()
# line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0]  # For line plot

# AXES PROPERTIES]
# ax.set_xlim3d([limit0, limit1])
# ax.set_xlabel('X(t)')
# ax.set_ylabel('Y(t)')
# ax.set_zlabel('time')
# ax.set_title('Trajectory of electron for E vector along [120]')

# plt.show()


def inputT():
    return dataSet
