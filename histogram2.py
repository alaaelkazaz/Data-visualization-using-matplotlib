from matplotlib import pyplot as plt
import numpy as np
fig,ax = plt.subplots(1,1)
a = np.array([22,87,5,7,8,10,9,54,11,20,51,5,79,31,27,16,17,18])
ax.hist(a, bins = [5,10,15,20,25])
ax.set_title("histogram of borrowed books frequency per week")
ax.set_xticks([5,10,15,20,25])
ax.set_xlabel('fees amount L.E')
ax.set_ylabel('Frequency of borrowing per week')
plt.show()