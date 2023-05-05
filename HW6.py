from __future__ import division
import numpy as np
l=1e-2
din=[]
with open('in.dta') as f:
	for line in f: # read rest of lines
        	din.append([float(x) for x in line.split()])
dout=[]
with open('out.dta') as g:
	for line in g: # read rest of lines
        	dout.append([float(x) for x in line.split()])
#print array
#print len(din)
dx1=[din[i][0] for i in range(len(din))]
dx2=[din[i][1] for i in range(len(din))]
dy=[din[i][2] for i in range(len(din))]
dx12=[dx1[i]**2 for i in range(len(din))]
dx22=[dx2[i]**2 for i in range(len(din))]
dx1x2=[dx1[i]*dx2[i] for i in range(len(din))]
dx1mx2=[abs(dx1[i]-dx2[i]) for i in range(len(din))]
dx1px2=[abs(dx1[i]+dx2[i]) for i in range(len(din))]
r=[dx1,dx2,dx12,dx22,dx1x2,dx1mx2,dx1px2]
X = np.column_stack(r+[[1]*len(r[0])])
b = np.linalg.lstsq(X.T.dot(X)+l*np.identity(len(r)+1),X.T.dot(dy))[0]
Ein=0
Eout=0
for i in range(len(din)):
	if (b[0]*dx1[i]+b[1]*dx2[i]+b[2]*dx12[i]+b[3]*dx22[i]+b[4]*dx1x2[i]+b[5]*dx1mx2[i]+b[6]*dx1px2[i]+b[7])*dy[i]<0:
		Ein+=1
Ein/=len(din)
dx1=[dout[i][0] for i in range(len(dout))]
dx2=[dout[i][1] for i in range(len(dout))]
dy=[dout[i][2] for i in range(len(dout))]
dx12=[dx1[i]**2 for i in range(len(dout))]
dx22=[dx2[i]**2 for i in range(len(dout))]
dx1x2=[dx1[i]*dx2[i] for i in range(len(dout))]
dx1mx2=[abs(dx1[i]-dx2[i]) for i in range(len(dout))]
dx1px2=[abs(dx1[i]+dx2[i]) for i in range(len(dout))]
for i in range(len(dout)):
	if (b[0]*dx1[i]+b[1]*dx2[i]+b[2]*dx12[i]+b[3]*dx22[i]+b[4]*dx1x2[i]+b[5]*dx1mx2[i]+b[6]*dx1px2[i]+b[7])*dy[i]<0:
		Eout+=1
Eout/=len(dout)
print Ein, Eout
