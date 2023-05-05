din=[]
with open('features.train.txt','r') as f:
	for line in f: # read rest of lines
        	din.append([float(x) for x in line.split()])
#print din
#-------------------------------------------
a=1
b=5
i=0
while 1:
	if int(din[i][0])!=a and int(din[i][0])!=b:
		din.pop(i)
	else:
		i+=1
	if i>=len(din):
		break
with open("HW8train"+str(a)+"all"+str(b)+".txt",'w') as g:
	for i in range(len(din)):
		g.write(str(1 if 1==int(din[i][0]) else -1)+" 1:"+str(din[i][1])+" 2:"+str(din[i][2])+"\n")
		
din=[]
with open('features.test.txt','r') as f:
	for line in f: # read rest of lines
        	din.append([float(x) for x in line.split()])
#print din
a=1
b=5
i=0
while 1:
	if int(din[i][0])!=a and int(din[i][0])!=b:
		din.pop(i)
	else:
		i+=1
	if i>=len(din):
		break
with open("HW8test"+str(a)+"all"+str(b)+".txt",'w') as g:
	for i in range(len(din)):
		g.write(str(1 if 1==int(din[i][0]) else -1)+" 1:"+str(din[i][1])+" 2:"+str(din[i][2])+"\n")
			
#for j in range(10):
#	with open("HW8train"+str(j)+"all.txt",'w') as g:
#		for i in range(len(din)):
#			g.write(str(1 if j==int(din[i][0]) else -1)+" 1:"+str(din[i][1])+" 2:"+str(din[i][2])+"\n")
#din=[]
#with open('features.test.txt','r') as f:
#	for line in f: # read rest of lines
#        	din.append([float(x) for x in line.split()])
#print din
#for j in range(10):
#	with open("HW8test"+str(j)+"all.txt",'w') as g:
#		for i in range(len(din)):
#			g.write(str(1 if j==int(din[i][0]) else -1)+" 1:"+str(din[i][1])+" 2:"+str(din[i][2])+"\n")
