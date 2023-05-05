#print "Hello, World!"
#Esta muito ineficiente
from __future__ import division
from cvxopt import matrix, solvers
import random
import numpy as np
import matplotlib.pyplot as plt
solvers.options['show_progress'] = False
w=[0,0,0]
m=0
b=0
def F(x):
	return M*x+b
def G(x):
	if w[2]>0:
		return (-w[1]/w[2])*x+(-w[0]/w[2])
	elif w[2]<0:
		return -((-w[1]/w[2])*x+(-w[0]/w[2]))
	else:
		return 0
def f(x,y):
	if y>M*x+b:
		return 1
	else:
		return -1
def hf(x,y):
	if y-M*x-b>0:
		return 1
	else:
		return -1
def hp(x,y,w):
	s=w[0]+w[1]*x+w[2]*y
	if s>0:
		return 1
	elif s<0:
		return -1
	else:
		return 0
def hq(x,y,w):
	s=wq[0]+wq[1]*x+wq[2]*y
	if s>0:
		return 1
	elif s<0:
		return -1
	else:
		return 0
def K(n,m):
	if n==m:
		return -1.
	else:
		return 0.
def L(x):
	return -((w[1]/w[2])*x+(w[0]/w[2])*b)
def Lq(x):
	return -((wq[1]/wq[2])*x+wq[0]/wq[2])
Perc=0
SNsv=0
H=1000
HP=10000
N=100
NJ=0
for j in range(H):
	print j
	while 1:
		x1=random.uniform(-1,1)
		y1=random.uniform(-1,1)
		x2=random.uniform(-1,1)
		y2=random.uniform(-1,1)
		M=((y2-y1)/(x2-x1))
		b=y1-M*x1
		#M=1
		#b=0
		q=0.4
		dx=[1,0,q,1-q,1-q,1,0,-q,q-1,q-1,-1]
		dy=[1,q,0,1,q,0,-q,0,-1,-q,0]
		dz=[f(dx[0],dy[0])]
		for i in range(N):
			dx.append(random.uniform(-1,1))
			dy.append(random.uniform(-1,1))
			dz.append(f(dx[i+1],dy[i+1]))
		if abs(sum(dz)-dz[0])!=N:
			break
	#perceptron algorithm
	w=[0,0,0]
	inter=[]
	SUM=0
	while 1:
		del inter[:]
		for i in range(N):
			if hp(dx[i],dy[i],w)!=f(dx[i],dy[i]):
				inter.append(i)
		if len(inter)==0:
			break
		u=random.randint(0,len(inter)-1)
		w2=[f(dx[inter[u]],dy[inter[u]])*t for t in [1,dx[inter[u]],dy[inter[u]]]]
		w=[q+e for q,e in zip(w,w2)]
		SUM=SUM+1
	h=0
	for i in range(HP):
		xint=random.uniform(-1,1)
		yint=random.uniform(-1,1)
		if hp(xint,yint,w)!=hf(xint,yint):
			h=h+1.
	Pp=h/HP
	#print Pp
	dx.pop(0)
	dy.pop(0)
	dz.pop(0)
	Qj=matrix([[dz[n]*dz[m]*(dx[n]*dx[m]+dy[n]*dy[m]) for m in range(N)] for n in range(N)])
	pj=matrix([-1. for m in range(N)])
	Gj=matrix([[K(n,m) for n in range(N)] for m in range(N)])
	hj=matrix([0. for n in range(N)])
	Aj=matrix([float(dz[m]) for m in range(N)], (1,N))
	bj=matrix(0.)
	sol=solvers.qp(Qj,pj,Gj,hj,Aj,bj)
	dc=sol['x']
	wq=[0,0,0]
	dcc=[]
	for k in range(N):
		dcc.append(dc[k])
	dzc=dz[:]
	dxc=dx[:]
	dyc=dy[:]
	kiu=0
	for k in range(N):
		if dcc[k-kiu]<1e-6:
			dcc.pop(k-kiu)
			dzc.pop(k-kiu)
			dxc.pop(k-kiu)
			dyc.pop(k-kiu)
			kiu+=1
	wq[1]=sum([dcc[m]*dzc[m]*dxc[m] for m in range(len(dcc))])
	wq[2]=sum([dcc[m]*dzc[m]*dyc[m] for m in range(len(dcc))])
	sf=[dzc[m]-wq[1]*dxc[m]-wq[2]*dyc[m] for m in range(len(dcc))]
	wq[0]=sum(sf)/len(sf)
	Nsv=len(dcc)
	h=0
	for i in range(HP):
		xint=random.uniform(-1,1)
		yint=random.uniform(-1,1)
		if hq(xint,yint,wq)!=hf(xint,yint):
			h=h+1.
	Ps=h/HP
	#print Ps
	if Ps<Pp:
		Perc+=1
	elif Ps==Pp:
		NJ+=1
	SNsv+=Nsv
	
Perc/=H
Perc*=100
SNsv/=H
print Perc, Perc+NJ/H, SNsv, NJ
