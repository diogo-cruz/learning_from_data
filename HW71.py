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
val=din[0:24]
din=din[25:34]
dx1=[din[i][0] for i in range(len(din))]
dx2=[din[i][1] for i in range(len(din))]
dy=[din[i][2] for i in range(len(din))]
dx12=[dx1[i]**2 for i in range(len(din))]
dx22=[dx2[i]**2 for i in range(len(din))]
dx1x2=[dx1[i]*dx2[i] for i in range(len(din))]
dx1mx2=[abs(dx1[i]-dx2[i]) for i in range(len(din))]
dx1px2=[abs(dx1[i]+dx2[i]) for i in range(len(din))]
dx1v=[val[i][0] for i in range(len(val))]
dx2v=[val[i][1] for i in range(len(val))]
dyv=[val[i][2] for i in range(len(val))]
dx12v=[dx1v[i]**2 for i in range(len(val))]
dx22v=[dx2v[i]**2 for i in range(len(val))]
dx1x2v=[dx1v[i]*dx2v[i] for i in range(len(val))]
dx1mx2v=[abs(dx1v[i]-dx2v[i]) for i in range(len(val))]
dx1px2v=[abs(dx1v[i]+dx2v[i]) for i in range(len(val))]
dx1o=[dout[i][0] for i in range(len(dout))]
dx2o=[dout[i][1] for i in range(len(dout))]
dyo=[dout[i][2] for i in range(len(dout))]
dx12o=[dx1o[i]**2 for i in range(len(dout))]
dx22o=[dx2o[i]**2 for i in range(len(dout))]
dx1x2o=[dx1o[i]*dx2o[i] for i in range(len(dout))]
dx1mx2o=[abs(dx1o[i]-dx2o[i]) for i in range(len(dout))]
dx1px2o=[abs(dx1o[i]+dx2o[i]) for i in range(len(dout))]
#Stuff a serio
r=[dx1,dx2,dx12,dx22,dx1x2,dx1mx2,dx1px2]
X = np.column_stack(r+[[1]*len(r[0])])
b = np.linalg.lstsq(X,dy)[0]
Eval=0
for i in range(len(val)):
	if (b[0]*dx1v[i]+b[1]*dx2v[i]+b[2]*dx12v[i]+b[3]*dx22v[i]+b[4]*dx1x2v[i]+b[5]*dx1mx2v[i]+b[6]*dx1px2v[i]+b[7])*dyv[i]<0:
		Eval+=1
Eval/=len(val)
Eout=0
for i in range(len(dout)):
	if (b[0]*dx1o[i]+b[1]*dx2o[i]+b[2]*dx12o[i]+b[3]*dx22o[i]+b[4]*dx1x2o[i]+b[5]*dx1mx2o[i]+b[6]*dx1px2o[i]+b[7])*dyo[i]<0:
		Eout+=1
Eout/=len(dout)
print 7, Eval, Eout
r=[dx1,dx2,dx12,dx22,dx1x2,dx1mx2]
X = np.column_stack(r+[[1]*len(r[0])])
b = np.linalg.lstsq(X,dy)[0]
Eval=0
for i in range(len(val)):
	if (b[0]*dx1v[i]+b[1]*dx2v[i]+b[2]*dx12v[i]+b[3]*dx22v[i]+b[4]*dx1x2v[i]+b[5]*dx1mx2v[i]+b[6])*dyv[i]<0:
		Eval+=1
Eval/=len(val)
Eout=0
for i in range(len(dout)):
	if (b[0]*dx1o[i]+b[1]*dx2o[i]+b[2]*dx12o[i]+b[3]*dx22o[i]+b[4]*dx1x2o[i]+b[5]*dx1mx2o[i]+b[6])*dyo[i]<0:
		Eout+=1
Eout/=len(dout)
print 6, Eval, Eout
r=[dx1,dx2,dx12,dx22,dx1x2]
X = np.column_stack(r+[[1]*len(r[0])])
b = np.linalg.lstsq(X,dy)[0]
Eval=0
for i in range(len(val)):
	if (b[0]*dx1v[i]+b[1]*dx2v[i]+b[2]*dx12v[i]+b[3]*dx22v[i]+b[4]*dx1x2v[i]+b[5])*dyv[i]<0:
		Eval+=1
Eval/=len(val)
Eout=0
for i in range(len(dout)):
	if (b[0]*dx1o[i]+b[1]*dx2o[i]+b[2]*dx12o[i]+b[3]*dx22o[i]+b[4]*dx1x2o[i]+b[5])*dyo[i]<0:
		Eout+=1
Eout/=len(dout)
print 5, Eval, Eout
r=[dx1,dx2,dx12,dx22]
X = np.column_stack(r+[[1]*len(r[0])])
b = np.linalg.lstsq(X,dy)[0]
Eval=0
for i in range(len(val)):
	if (b[0]*dx1v[i]+b[1]*dx2v[i]+b[2]*dx12v[i]+b[3]*dx22v[i]+b[4])*dyv[i]<0:
		Eval+=1
Eval/=len(val)
Eout=0
for i in range(len(dout)):
	if (b[0]*dx1o[i]+b[1]*dx2o[i]+b[2]*dx12o[i]+b[3]*dx22o[i]+b[4])*dyo[i]<0:
		Eout+=1
Eout/=len(dout)
print 4, Eval, Eout
r=[dx1,dx2,dx12]
X = np.column_stack(r+[[1]*len(r[0])])
b = np.linalg.lstsq(X,dy)[0]
Eval=0
for i in range(len(val)):
	if (b[0]*dx1v[i]+b[1]*dx2v[i]+b[2]*dx12v[i]+b[3])*dyv[i]<0:
		Eval+=1
Eval/=len(val)
Eout=0
for i in range(len(dout)):
	if (b[0]*dx1o[i]+b[1]*dx2o[i]+b[2]*dx12o[i]+b[3])*dyo[i]<0:
		Eout+=1
Eout/=len(dout)
print 3, Eval, Eout

