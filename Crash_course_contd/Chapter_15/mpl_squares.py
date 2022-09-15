#       W   E   L   C   O   M   E       T   O       M   A   T   P   L   O   T   L   I   B
import matplotlib.pyplot as plt

# A sample data in a list
values = [1,2,3,4,5]
squares = [1,4,9,16,25]

#Using a built-in style e.g seaborn style
plt.style.use("seaborn")

fig,ax = plt.subplots()
ax.plot(values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=6)

plt.show()