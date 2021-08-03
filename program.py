#The program count the sum of squares of numbers from 1 to 9

sum=0
for i in range(1,10):
	print(i*i, end='')
	sum+=i
	
print("The sum is:{}".format(sum))
