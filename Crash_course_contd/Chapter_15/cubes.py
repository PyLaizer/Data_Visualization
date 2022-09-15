#Exercise 15.1 & 15.2

import matplotlib.pyplot as plt


# x_values = [1,2,3,4,5]
# y_values = []
# plt.style.use("seaborn")
# for x in x_values:
#     y = x**3
#     y_values.append(y)

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")
fig,ax = plt.subplots()
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Reds, s=5) 

#Set chart title and label axes
ax.set_title("Cubic Numbers",fontsize=20)
ax.set_xlabel("Values", fontsize=10)
ax.set_ylabel("Cubed Values", fontsize=10)

plt.show()