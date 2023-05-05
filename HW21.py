from __future__ import division
import random
import numpy as np
Megasum=0
Psum=0
H=1000
N=10
for j in range(H):
	x1=random.uniform(-1,1)
	y1=random.uniform(-1,1)
	x2=random.uniform(-1,1)
	y2=random.uniform(-1,1)
	m=((y2-y1)/(x2-x1))
	b=y1-m*x1
	def f(x,y):
		if y>m*x+b:
			return 1
		else:
			return -1
	dx=[1]
	dy=[1]
	for i in range(N):
		dx.append(random.uniform(-1,1))
		dy.append(random.uniform(-1,1))
		
	Dx=dx[:]
	Dy=dy[:]
	del Dx[0]
	del Dy[0]
	Dz=[]
	for i in range(N):
		Dz.append(f(Dx[i],Dy[i]))
	r=[Dx,Dy]
	X = np.column_stack(r+[[1]*len(r[0])])
	bt = np.linalg.lstsq(X,Dz)[0]
	print bt
	w=[bt[2],bt[0],bt[1]]
	
	def h(x,y,w):
		s=w[0]+w[1]*x+w[2]*y
		if s>0:
			return 1
		elif s<0:
			return -1
		else:
			return 0
	#perceptron algorithm
	inter=[]
	SUM=0
	while 1:
		del inter[:]
		for i in range(N):
			if h(dx[i],dy[i],w)!=f(dx[i],dy[i]):
				inter.append(i)
		if len(inter)==0:
			break
		u=random.randint(0,len(inter)-1)
		w2=[f(dx[inter[u]],dy[inter[u]])*t for t in [1,dx[inter[u]],dy[inter[u]]]]
		w=[q+e for q,e in zip(w,w2)]
		SUM=SUM+1
	mm=-w[1]/w[2]
	bb=-w[0]/w[2]
	Megasum=Megasum+SUM
Megasum=Megasum/H
print Megasum	
#print SUM

