b = int(raw_input("Enter base(1 to 10): "))
n = int(raw_input("Enter the number to convert: "))
num = n
sum = 0
a = []

while n > 0:
  rem = n%b
  n = n / b
  a.append(rem)

for x in range(len(a)):
  sum = sum + a[x]* 10 **(x)

print "Conversion of %d = %d" %(num,sum)
