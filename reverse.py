n = int(raw_input("Enter the number to reverse: "))
num = n
sum = 0
a = []

while n > 0:
  rem = n%10
  n = n / 10
  a.append(rem)

for x in range(len(a)):
  sum = sum + a[x]* 10 **(len(a)-1-x)

print "Reverse of %d = %d" %(num,sum)
