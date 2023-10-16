import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def KNN(tdata,unknown ):






# load data
data1 = np.loadtxt("trainClass1.dat")
data2 = np.loadtxt("trainClass2.dat")
data3 = np.loadtxt("trainClass3.dat")
data4 = np.loadtxt("trainClass4.dat")

trainingdata = [data1, data2, data3, data4]

unclassifieddata= np.loadtxt("unknown.dat")

fig, ax = plt.subplots()
ax = fig.add_subplot(projection='3d')
ax.scatter(data1[:,0], data1[:,1], data1[:,2])
ax.scatter(data2[:,0], data2[:,1], data2[:,2])
ax.scatter(data3[:,0], data3[:,1], data3[:,2])
ax.scatter(data4[:,0], data4[:,1], data4[:,2])
plt.show()







