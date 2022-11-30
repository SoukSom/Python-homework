factorialIP = int (input ("Input a number: "))
factorail = 1
for j in range (1, factorialIP+1):
   factorail = factorail * j
def getSum(n):
    sum = 0
    for i in str(n): 
      sum += int(i)      
    return sum
print("Output:", (getSum(factorail)))