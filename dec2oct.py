n = int(raw_input("Enter the number to convert into octal: "))
num = n
sum = 0
a = []

while n > 0:
  rem = n%7
  n = n / 7
  a.append(rem)

for x in range(len(a)):
  sum = sum + a[x]* 10 **(x)

print "Octal of %d = %d" %(num,sum)
