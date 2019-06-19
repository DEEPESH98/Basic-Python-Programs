import matplotlib.pyplot as plt
import numpy as np
import time

x=[4,7,8,9,11,5]
y=[13,23,5,7,9,6]
player=['virat','dhoni','vijay','dhawan']
runs=[120,130,150,33]
exp=[0.1,1,2,0.2]

#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
plt.pie(runs,labels=player,explode=exp,shadow=True,autopct='%1.1f%%')
plt.grid(color='green')
#plt.legend() # to show lables with plot
plt.show()
