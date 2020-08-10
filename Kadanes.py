#kadane's algorithm
a=[-2,-3,4,-1,-2,1,5,-3]
#set max_sum is least than any number in the array
max_sum=min(a)-1
max_till=0
for i in range(len(a)):
	max_till=max_till+a[i]
	if max_sum<max_till:
		max_sum=max_till
	if max_till<0:
		max_till=0
print(max_sum)

"""""""""""""""""""
""" Output is 7 """
"""""""""""""""""""
