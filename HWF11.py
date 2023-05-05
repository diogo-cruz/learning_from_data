import numpy as np
import matplotlib.pyplot as plt
data=[[1,0],[0,1],[0,-1],[-1,0],[0,2],[0,-2],[-2,0]]
yd=[-1,-1,-1,1,1,1,1]
dataz=[[data[i][1]*data[i][1]-2*data[i][0]-1,data[i][0]*data[i][0]-2*data[i][1]+1] for i in range(len(data))]
#print dataz
z=['red','blue','green','black','grey','pink','brown','purple','yellow','orange']
#for j in range(10):
#	plt.scatter(datax[j],datay[j],s=20, c=z[j])
datazr=[dataz[i] for i in range(len(dataz)) if yd[i]==1]
datazb=[dataz[i] for i in range(len(dataz)) if yd[i]==-1]
#print datazr
#print datazb
plt.scatter([datazr[i][0] for i in range(len(datazr))],[datazr[i][1] for i in range(len(datazr))],s=20, c=z[0])
plt.scatter([datazb[i][0] for i in range(len(datazb))],[datazb[i][1] for i in range(len(datazb))],s=20, c=z[1])
#x = np.linspace(-0., 0.6, 100)
#y = np.linspace(-8.0, 0.0, 100)
#X, Y = np.meshgrid(x,y)
#btz=[ 1.39444919,  0.47743748,  0.77188926, -0.12728014, -0.05660804,  0.04520773]
#btzl=[ 1.27114559,  2.25478075,  0.82549599, -0.51572027, -5.84769754,  0.03777864]
#F = btz[0]+btz[1]*X+btz[2]*Y+btz[3]*X*Y+btz[4]*X**2 + btz[5]*Y**2
#Fl = btzl[0]+btzl[1]*X+btzl[2]*Y+btzl[3]*X*Y+btzl[4]*X**2 + btzl[5]*Y**2
#plt.contour(X,Y,F,[0], colors=z[0])
#plt.contour(X,Y,Fl,[0], colors=z[1])
plt.show()
