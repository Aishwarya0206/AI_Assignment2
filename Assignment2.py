#Get input from the user(i.e, the end of the fibonacci sequence number)
num = int(input("Enter the number:"))
#intialize a & b as 0 & 1
a = 0
b = 1
#intialize sum to 1
sum = 0
#Execute the loop when sum is less the number given by the user
while(sum<num):
    #print the sum
    print(sum,end=' ')
    #Assign b to a
    a = b
    #Assign sum to b
    b = sum
    #Assign the summation of a & b in sum
    sum = a+b
