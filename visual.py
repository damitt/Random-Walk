
from randomWalk import random_walk
import matplotlib.pyplot as plt


while True:
    walk1 = random_walk()
    walk1.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(walk1.x_values, walk1.y_values)
    plt.show()

    next = input()
    if next != 'yes':
        break



# walk1 = random_walk()
# walk1.fill_walk()

# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.scatter(walk1.x_values, walk1.y_values)
# plt.show()

