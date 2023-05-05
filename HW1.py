#print "Hello, World!"
#Esta muito ineficiente
import random
Megasum=0
Psum=0
H=1000
HP=100
N=100
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
	w=[0,0,0]
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
		#print w
		#wait=input("")
		SUM=SUM+1
	mm=-w[1]/w[2]
	bb=-w[0]/w[2]
	#xU=(b-bb)/(mm-m)
	def F(x):
		return m*x+b
	def G(x):
		return mm*x+bb
	h=0
	for i in range(HP):
		xint=random.uniform(-1,1)
		yint=random.uniform(-1,1)
		if (yint>F(xint) and yint<G(xint)) or (yint<F(xint) and yint>G(xint)):
			h=h+1.
	P=h/HP
	#print m,'x+(',b,')'
	#print mm,'x+(',bb,')'
	#if abs(-m+b)<=1 and abs(-mm+bb)<=1 and abs(m+b)<=1 and abs(mm+bb)<=1:
	#	if -1<xU<1:
	#		P=(abs(-m+b+mm-bb)*(xU+1)+abs(m+b-mm-bb)*(1-xU))/8
	#	else:
	#		P=(abs(-m+b+mm-bb)+abs(m+b-mm-bb))/4
	Megasum=Megasum+SUM
	Psum=Psum+P
Megasum=Megasum/H
Psum=Psum/H
print Megasum
print Psum	
#print SUM

