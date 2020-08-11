#PYTHON CODE FOR PASCAL TRIANGLE
#space complexity O(1)
#Time Complexity O(m*n)

n=int(input("Enter the length of pascal triangle: "))
for line in range(1,n+1):
	num=1
	for i in range(1,line+1):
		print(num,end=" ")
		num=int(num*(line-i)/i)
	print("")
