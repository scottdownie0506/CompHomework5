#!/usr/bin/env python
# coding: utf-8

# In[3]:


# question 1

import matplotlib.pyplot as plt
import numpy as np

x1 = ([0, 4])
x2 = ([0, 4])
x3 = ([0, 4])

y1 = ([1, 5])
y2 = ([5, 9])
y3 = ([9, 13])

plt.plot(x1, y1, linewidth = '1.5')
plt.plot(x2, y2, linewidth = '1.5')
plt.plot(x3, y3, linewidth = '1.5')
plt.xlabel('X Label')
plt.ylabel('Y Label')


# In[12]:


# question 2

mu, sigma = 0, 0.2
s = np.random.normal(mu, sigma, 800)
plt.hist(s)
plt.show()


# In[26]:


# question 3

mydic = {"Apples": 45, "Bananas":25, "Cherries":15, "Dates":20}

fruit = []
count = []

for k in mydic:
    fruit.append(k)
for k in mydic.values():
    count.append(k)
print(fruit)
print(count)
xplode = [0.1, 0.1, 0.1, 0.1]

plt.pie(count, labels = fruit, explode = xplode)
plt.legend(bbox_to_anchor = (1.05, 1.0), loc= "upper left")
plt.show()

plt.bar(fruit, count)
plt.show()


# In[38]:


# question 4
# STILL NEED LEGEND 

marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # this is x-axis values
math_marks = [88, 92, 80, 89, 90, 80, 60, 88, 80, 84] # this is the math marks
science_marks = [75, 59, 69, 48, 65, 56, 32, 45, 20, 30] # this is the science marks

plt.scatter(marks_range, math_marks, color = 'r', label = "Art Marks")
plt.scatter(marks_range, science_marks, color = 'g', label = "Science Marks")

plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.title('Scatter Plot')
plt.legend()
plt.show()


# In[11]:


# question 5

# plot 1

x = [8, 2, 8, 9, 0, 4, 6, 8, 11, 1]
y = [5, 9, 6, 4, 5, 6, 2, 4, 2, 0] 

plt.subplot(1, 4, 1)
plt.scatter(x,y)
plt.title('Grades')

# plot 2

x1 = ([0, 1, 2, 3, 4, 5])
x2 = ([0, 1, 2, 3, 4])

y1 = ([1, 5, 8, 11, 2, 5])
y2 = ([5, 9, 2, 10, 6])

plt.subplot(1, 4, 2)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title('Death Rates')

# plot 3

letters = ["A", "B", "C", "D"]
count = [12, 10, 3, 9]
plt.subplot(1, 4, 3)
plt.bar(letters, count)
plt.title('Boots')

# plot 4

vegetables = ["Corn", "Lettuce", "Cucumber", "Radish"]
xplode = [0.1, 0.1, 0.1, 0.1]
plt.subplot(1, 4, 4)
plt.pie(count, labels = vegetables, explode = xplode)
plt.title('Vegetables')

plt.show()


# In[ ]:




