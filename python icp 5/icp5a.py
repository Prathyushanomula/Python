#import matplotlib.pyplot as plot
#from sklearn import linear_model
import numpy as np

#x=[0,1,2,3,4,5,6,7,8,9]
#y=[1,3,2,5,7,8,8,9,10,12]

#def show_plots(x,y):
   # linear_mod=linear_model.LinearRegression()
    #x = np.reshape(x, (len(x), 1))  # converting to matrix of n X 1
    #y = np.reshape(y, (len(y), 1))
    #linear_mod.fit(x, y)  # fitting the data points in the model
    #plot.scatter(x, y, color='red')  # plotting the initial datapoints
    #plot.plot(x, linear_mod.predict(x), color='blue', linewidth=3)  # plotting the line made by linear regression
    #plot.show()
    #return

#show_plots(x, y)
# image of the plot will be generated. Save it if you want and then Close it to continue the execution of the below code.


import numpy as np
import matplotlib.pyplot as plt

#Take two arrays
x=np.array([2.9,6.7,4.9,7.9,9.8,6.9,6.1,6.2,6,5.1,4.7,4.4,5.8])
y=np.array([4,7.4,5,7.2,7.9,6.1,6,5.8,5.2,4.2,4,4.4,5.2])

#Calculate the means of two arrays
meanx=np.mean(x)
meany=np.mean(y)

#Calculate the distance between the points  from mean and add them
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
m=num/den

#Calculate the intercept of the line
intercept=meany-(m*meanx)

#Write the line equation and plot the graph
val=(m*x)+intercept
plt.scatter(x,y)
plt.plot(x,val)
plt.show()
