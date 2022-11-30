Input = int(input("input number:"))
def getSum(Input):
    sum = 0
    for i in str(Input): 
      sum += int(i)  
      print    
    return sum

print("Output:", (getSum(Input)))