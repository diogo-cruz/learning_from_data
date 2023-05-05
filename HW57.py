from math import exp
def E(w):
	return (w[0]*exp(w[1])-2*w[1]*exp(-w[0]))**2
def Gu(w):
	return 2*(w[0]*exp(w[1])-2*w[1]*exp(-w[0]))*(exp(w[1])+2*w[1]*exp(-w[0]))
def Gv(w):
	return 2*(w[0]*exp(w[1])-2*exp(-w[0]))*(w[0]*exp(w[1])-2*w[1]*exp(-w[0]))
w=[1,1]
n=0.1
i=0
while i<15:
	print i, w, E(w)
	w[0]=w[0]-n*Gu(w)
	w[1]=w[1]-n*Gv(w)
	i=i+1
print i, w, E(w)
