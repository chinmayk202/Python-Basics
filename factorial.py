def factorial(n):
  result = 1
  for x in range(n):
    result = result * (x+1)
  return result

num = int(raw_input("Enter the number to get Factorial: "))

print "Factorial %d = %d" %(num,factorial(num))
