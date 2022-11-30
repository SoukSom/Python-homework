time = int(input("Enter Number:"))

hours = time // 60
minutes = time % 60

print("Output: ", (str(hours) + ":" + str(minutes)))