#The program count the sum of squares of numbers from 1 to number chosen by user

sum=0
for i in range(1,int(input())):
	print(i*i, end='')
	sum+=i
print("The sum is:{}".format(sum))
