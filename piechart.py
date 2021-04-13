import matplotlib.pyplot as plt
import numpy as np
# Categories pie chart 
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
categories = ['Religious', 'Scientific', 'Fiction', 'Novels', 'Classics']
students = [23,17,35,29,12]
ax.pie(students, labels = categories,autopct='%1.2f%%')
plt.show()