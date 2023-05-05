	
	x=np.arange(-1.,1.1)
	p1x=[]
	m1x=[]
	p1y=[]
	m1y=[]
	for k in range(N):
		if dz[k]>0:
			p1x.append(dx[k])
			p1y.append(dy[k])
		else:
			m1x.append(dx[k])
			m1y.append(dy[k])
	y=F(x)
	ypla=G(x)
	yp=Lq(x)
	plt.plot(x,y)
	plt.plot(x,ypla)
	plt.plot(x,yp)
	plt.scatter(p1x,p1y,s=40,c='red')
	plt.scatter(m1x,m1y,s=40,c='blue')
	plt.ylim(-1.1,1.1)
	plt.xlim(-1.1,1.1)
	plt.show()
	
