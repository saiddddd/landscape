import numpy as np
import plotly.graph_objects as go

def ObjectiveFunction(x):
    # List of your constraints
    const1 = x[1] <= 3.2 or x[1] >= 6.4
    const2 = (x[0] ** 2 + x[1] ** 2) >= 1
    const3 = x[0] != x[1]

    if const1 and const2 and const3:
        o = sum(np.power(x, 2))  # Sphere test function
    else:
        # The solution IS NOT feasible (infeasible)
        o = sum(np.power(x, 2)) + 200
    
    return o

fobj = ObjectiveFunction

x = np.arange(-10, 10, 0.05)
y = np.arange(-10, 10, 0.05)

x_new, y_new = np.meshgrid(x, y)
o = np.zeros_like(x_new)

for i in range(x_new.shape[0]):
    for j in range(x_new.shape[1]):
        currentX = [x_new[i, j], y_new[i, j]]
        o[i, j] = fobj(currentX)

fig = go.Figure(data=[go.Surface(x=x_new, y=y_new, z=o)])
fig.update_layout(scene=dict(xaxis_title='x_1', yaxis_title='x_2', zaxis_title='Objective Value'))
fig.show()