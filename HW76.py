from __future__ import division
import random
E1=0
E2=0
E=0
B=1000
for i in range(B):
	e1=random.uniform(0,1)
	e2=random.uniform(0,1)
	e=min(e1,e2)
	E1+=e1
	E2+=e2
	E+=e
E1/=B
E2/=B
E/=B
print E1, E2, E
	
