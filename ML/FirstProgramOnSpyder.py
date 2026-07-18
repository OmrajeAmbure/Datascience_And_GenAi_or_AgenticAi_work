import matplotlib.pyplot as plt

labels = ['Python','Java','C++','JavaScript']
data = [40,25,20,15]

plt.pie(data,labels=labels,autopct='%1.1f%%')

plt.title('Programming Langauge Usage ')

plt.show()