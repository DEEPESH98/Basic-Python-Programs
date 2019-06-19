import matplotlib.pyplot as plt
#only loading python orfiented libary
​
​
x=[2,3]
x1=[4,3,8]
y1=[2,9,7]
y=[9,5]
​
plt.xlabel("time")
plt.ylabel("speed")
plt.plot(x,y,label="water") # plot funtion dono jode ke state line bana ta he
plt.plot(x1,y1,label="sand")
plt.bar(x1,y1,color="pink")
plt.grid(color="green")
plt.legend() # to show lables with plot
plt.xlim(0,12) # TO SHOW MIN and max number in axis
plt.ylim(0,15)
plt.show()
