#Exercise 15.10
import matplotlib.pyplot as plt
from die import Die

#Creating the die instance
die_1 = Die()
die_2 = Die()

results = []
for num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)


frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for num in range(2, max_result+1):
    frequency = results.count(num) 
    frequencies.append(frequency) 

#MAKE data
x = [num for num in range(2, max_result+1)]
y = frequencies     

plt.style.use('seaborn')
fig,ax = plt.subplots(figsize=(8,6))
ax.bar(x,y, width=1, edgecolor='white', linewidth=1)

# Setting  the labels and title
ax.set_title("Rolling two D6s 100 times", fontsize=24)
ax.set_xlabel("Outcomes", fontsize=10)
ax.set_ylabel("Frequency of Outcomes", fontsize=10)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=6)

#Set range of tick label
ax.set(xticks=range(2,max_result+1), yticks=range(2,20,2))

plt.show()        