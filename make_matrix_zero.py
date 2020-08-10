import numpy as np
#define the array arr
arr=np.array([[0,4,1,0],
                       [3,2,1,5],
                       [1,0,7,2]])
row,col=np.shape(arr)
#create flags for row and column
first_row=bool(0)
first_col=bool(0)
#step1: if 0 present in any col or row make entire col or row 0
for i in range(row):
	if arr[i][0]==0:
		first_col=1
for j in range(col):
	if arr[0][j]==0:
		first_row=1
#step 2: iterate matrix from a[1][1] till last
# if a[i][j] is 0 make a[i][0] and a[0][j]=0
for i in range(1,row):
	for j in range(1,col):
		if arr[i][j]==0:
			arr[i][0]=0
			arr[0][j]=0
#again iterate same as step 2 this time if 
#a[i][0] and a[0][j]=0 make a[i][j]=0
for i in range(1,row):
	for j in range(1,col):
		if arr[i][0]==0 or arr[0][j]==0:
			arr[i][j]=0
#check row flag if true make all elements of 
#first row 0 and same for col 
if first_row==True:
	for j in range(col):
		arr[0][j]=0
if first_col==True:
	for i in range(row):
		arr[i][0]=0
print(arr)
