import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Keep making new walks, as long as the program is active
while True:
    #Making a random walk instance
    rw = RandomWalk()
    rw.fill_walk()

    #Plotting the points of the walk
    plt.style.use('classic')
    
    fig, ax = plt.subplots(figsize=(16,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolors='none', s=10)
    
    ax.scatter(0,0, c='red',edgecolors='none',s=50)
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c='blue',edgecolors='none', s=50)

    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break