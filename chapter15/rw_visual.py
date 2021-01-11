import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    x_values = rw.x_values
    y_values = rw.y_values
    point_numbers = list(range(rw.num_points))
    plt.scatter(x_values, y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(x_values[-1], y_values[-1], c='red', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk?（y/n）:")
    if keep_running == 'n':
        break

