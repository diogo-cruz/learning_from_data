from __future__ import division
import random
from math import sqrt, exp, log
H=100
N=100
Mil=1000
n=0.01
Set=[i for i in range(N)]
AvEp=0
AvEout=0
def G(w,k):
	a=-dz[k]/(1+exp(dz[k]*(w[0]+w[1]*dx[k]+w[2]*dy[k])))
	return [a,a*dx[k],a*dy[k]]
def Y(x,y):
	if y>m*x+b:
		return 1
	else:
		return -1
def g(x,y):
	return w[0]+w[1]*x+w[2]*y#>=0:
	#	return 1
	#else:
	#	return -1
def D(w,w0):
	return sqrt(sum([(w[i]-w0[i])**2 for i in range(len(w))]))
for j in range(H):
	dx=[]
	dy=[]
	dz=[]
	x1=random.uniform(-1,1)
	y1=random.uniform(-1,1)
	x2=random.uniform(-1,1)
	y2=random.uniform(-1,1)
	m=((y2-y1)/(x2-x1))
	b=y1-m*x1
	for i in range(N):
		dx.append(random.uniform(-1,1))
		dy.append(random.uniform(-1,1))
		dz.append(Y(dx[i],dy[i]))
	#Logistic regression algorithm
	w=[0,0,0]
	w0=[1,1,1]
	Err=[G(w,i) for i in range(N)]
	#print Err[0]
	#Verificar esta linha
	Gin=[sum(i)/N for i in zip(*Err)]
	w=[w[i]-n*Gin[i] for i in range(len(w))]
	print j
	ep=0
	while D(w,w0)>=0.01:
		 random.shuffle(Set)
		 w0=w[:]
		 for i in range(N):
		 	Err[Set[i]]=G(w,Set[i])
		 	Gin=[sum(i)/N for i in zip(*Err)]
		 	w=[w[i]-n*Gin[i] for i in range(len(w))]
		 	#print "---------  ", w
		 ep+=1
	#print ep
	AvEp+=ep
	Eout=0
	for i in range(Mil):
		x=random.uniform(-1,1)
		y=random.uniform(-1,1)
		#if Y(x,y)!=g(x,y):
		Eout+=log(1+exp(-Y(x,y)*g(x,y)))
	Eout/=Mil
	#print Eout
	AvEout+=Eout
AvEout/=H	
AvEp/=H
print AvEout, AvEp

