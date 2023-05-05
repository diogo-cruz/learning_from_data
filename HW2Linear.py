#print "Hello, World!"
#Esta muito ineficiente
from __future__ import division
import random
import numpy as np
H=1000
N=100
dx=[]
dy=[]
dz=[]
Med=0
x1=0
y1=0
x2=1
y2=1
m=((y2-y1)/(x2-x1))
b=y1-m*x1
def f(x,y):
	if y>m*x+b:
		return 1
	else:
		return -1
for i in range(N):
	dx.append(random.uniform(-1,1))
	dy.append(random.uniform(-1,1))
for j in range(H):
	x1=random.uniform(-1,1)
	y1=random.uniform(-1,1)
	x2=random.uniform(-1,1)
	y2=random.uniform(-1,1)
	m=((y2-y1)/(x2-x1))
	b=y1-m*x1
	#print m, b
	dz=[]
	for i in range(N):
		dz.append(f(dx[i],dy[i]))
#Linear regression
	#dx=[1,1,2,2]
	#dy=[1,2,1,2]
	#dz=[1,1,1,1]
	#for i in range(len(dx)):
	#	print dx[i],dy[i],dz[i]
	#print f(1,1), f(-1,-1)
	r=[dx,dy]
	X = np.column_stack(r+[[1]*len(r[0])])
	beta_hat = np.linalg.lstsq(X,dz)[0]
	print beta_hat
	def gh(s):
		if s>0:
			return 1
		else:
			return -1
	res=[abs(dz[i]-gh(np.dot(X,beta_hat)[i])) for i in range(len(dz))]
	Ein=sum(res)/(2*N)	
	Med+=Ein
Med/=H
print Med
