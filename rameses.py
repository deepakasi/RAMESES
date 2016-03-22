#python3
######################Assignment 2#########################################
####Step1:Take input n from command and build NxN matrix###################
####Step2:check the matrix element if it is filled,if filled skip else compute the heuristic by calling sum()#######
####step3:Call col() to function to compute number of empty spaces on filling the position,likewise call row() and diagonal d()##########
####step4:compute heuristic for all position and choose the position with maximum value of col and row and which doesn't affect diagonal else maximum diagonal value###
####step5:output the favourable position################
####step6:Exit on filling the row,column and diagonal and print Exit message Game over#########
######################End###################################################
import time
import statistics
import sys
n=int(sys.argv[1])
s=list(sys.argv[2])
tt=time.time()#float(sys.argv[3])
Matrix = [[0 for x in range(n)] for x in range(n)] #Creating a matrix of size NxN
val={} #List to old the value of heuristic function
k=0 #value to initialize the matrix
for i in range (0,n): #initializing the matrix
	for j in range(0,n):
		Matrix[i][j]=s[k]
		k=k+1
def row(i,j): # checking row to compute heuristic
	count=0
	for k in range(0,n):
		if(Matrix[i][k]=='.'):
			count=count+1
	return count-1
def col(i,j): #checking column to compute heuristic
	count=0
	for k in range(0,n):
		if(Matrix[k][j]=='.'):
			count=count+1
	return count-1
def d(i,j): # checking diagonal to compute heuristic
	count1=0
	count2=0
	if(i==j):
		for k in range(0,n):
			if(Matrix[k][k]=='.'):
				count1=count1+1
		return count1-1
	if i+j==n-1:
		for k in range(0,n):
			if Matrix[k][n-1-k]=='.':
				count2=count2+1
		return count2-1	
	return max(count1-1,count2-1)
maxlist=[]
def sum(): #function to calculate the heuristic
	max=-90
	for i in range(0,n*n):
		list=val[i]
		if(list[2]>0 and list[3]>0):
			sum=list[2]+list[3]
			if sum>max:
				max=sum
				del maxlist[:]
				maxlist.append(i)
			elif sum==max:
				maxlist.append(i)
def dmove(): #function to decide if the move is on diagonal element
	dmax=-2
	d=-1
	for i in range(0,len(maxlist)):
		l=maxlist[i]
		if(val[l][4]<0):
			return l
		else:
			if(dmax<val[l][4]):
				dmax=val[l][4]
				d=l
	return d
k=0
timeout=time.time()+tt
for i in range(0,n):
	for j in range(0,n):
		if(time.time()>timeout):
			print("timeout!!")
			exit ()
		if(Matrix[i][j]=='.'):
			value=[i,j,col(i,j),row(i,j),d(i,j)]
			val[k]=value	
			k=k+1
		else:
			value=[i,j,-1,-1,-1]
			val[k]=value
			k=k+1
	
	if(time.time()-tt>float(sys.argv[3])): ##################Timeout check################### 
	
		print("Timeout!!")
		break

sum()
if(len(maxlist)>1): ##decide on the next move
	m=dmove()
	print("Recommended Move is row",val[m][0]+1,"Column",val[m][1]+1)
	newind = (val[m][0]*n)+(val[m][1]+1)
	s[newind-1]='x'
	print(''.join(s))
else:
	if(len(maxlist)==0):
		print("GAME OVER!! :(")
	else:	
		m=maxlist[0]
		print("Recommended Move is row",val[m][0]+1,"Column",val[m][1]+1)
		newind1 = (val[m][0]*n)+(val[m][1]+1)
		s[newind1-1]='x'
		print(''.join(s))



