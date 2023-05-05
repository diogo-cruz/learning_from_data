from __future__ import division
import random
DezMil=100000
Mil=1000
Dez=10
V1=0
Vr=0
Vm=0
for j in range(DezMil):
	Coin=[[random.randint(0,1) for r in range(Dez)] for t in range(Mil)]
	Sum=[sum(Coin[t]) for t in range(Mil)]
	#print Coin
	C1=Coin[0]
	Cr=Coin[random.randint(0,Mil-1)]
	#print C1
	#print Cr
	#print Sum
	Max=0
	for i in range(Mil):
		if Sum[i]>Max:
			Max=i
	Cm=Coin[Max]
	#print Cm
	v1=sum(C1)/Dez
	vr=sum(Cr)/Dez
	vm=sum(Cm)/Dez
	V1+=v1
	Vr+=vr
	Vm+=vm
	print j
V1/=DezMil
Vr/=DezMil
Vm/=DezMil
print V1,Vr,Vm
#print v1, vr, vm
