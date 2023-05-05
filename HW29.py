#print "Hello, World!"
#Esta muito ineficiente
from __future__ import division
import random
import numpy as np
H=300
N=1000
Med=0
def f(x,y):
	P=random.uniform(0,1)
	if x**2+y**2-0.6>0:
		if P>0.1:
			return 1
		else:
			return -1
	elif x**2+y**2-0.6<0:
		if P<0.1:
			return 1
		else:
			return -1
	else:
		return 0
FIM=[0,0,0,0,0,0]
for j in range(H):
	dx=[]
	dy=[]
	dz=[]
	dx2=[]
	dy2=[]
	dxy=[]
	for i in range(N):
		dx.append(random.uniform(-1,1))
		dy.append(random.uniform(-1,1))
		dz.append(f(dx[i],dy[i]))
		dx2.append(dx[i]*dx[i])
		dy2.append(dy[i]*dy[i])
		dxy.append(dx[i]*dy[i])
#Linear regression
	r=[dx,dy,dxy,dx2,dy2]
	X = np.column_stack(r+[[1]*len(r[0])])
	beta_hat = np.linalg.lstsq(X,dz)[0]
	print j, beta_hat
	def gh(s):
		if s>0:
			return 1
		else:
			return -1
	res=[abs(dz[i]-gh(np.dot(X,beta_hat)[i])) for i in range(len(dz))]
	Ein=sum(res)/(2*N)	
	Med+=Ein
	FIM=[FIM[i]+beta_hat[i] for i in range(len(beta_hat))]
Med/=H
FIM=[FIM[i]/H for i in range(len(FIM))]
print Med, FIM
