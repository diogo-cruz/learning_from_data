from math import exp
def E(w):
	return (w[0]*exp(w[1])-2*w[1]*exp(-w[0]))**2
def G(w):
	return [2*(w[0]*exp(w[1])-2*w[1]*exp(-w[0]))*(exp(w[1])+2*w[1]*exp(-w[0])),2*(w[0]*exp(w[1])-2*exp(-w[0]))*(w[0]*exp(w[1])-2*w[1]*exp(-w[0]))]
w=[1,1]
n=0.1
i=0
while E(w)>=1e-14:
	print i, w, E(w)
	w=[w[0]-n*G(w)[0],w[1]-n*G(w)[1]]
	i=i+1
print i, w, E(w)
