import numpy as np
import matplotlib.pyplot as plt

data = [[30, 25, 50, 20],
[40, 23, 51, 17],
[35, 22, 45, 19]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#ax.bar(x, height, width, bottom, align)
ax.set_ylabel('Numbers')
ax.set_title('Borrow numbers through 3 months')
ax.set_xticks([0,2,4,6])
ax.set_xticklabels(['zero','two','four','six'])
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
ax.legend(labels=['scientific', 'Fiction','Novels'])
plt.show()
