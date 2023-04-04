import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()
while True:
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9),dpi=126)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values,  linewidth=1,zorder=1)
    ax.set_aspect('equal')
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100,zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100,zorder=2)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    # Keep making new walks, as long as the program is active.
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
