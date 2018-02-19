num = int(raw_input("Enter the number to reverse: "))

a = []
b = []
rem = 0.0
for x in range(100):
  rem = num % 10**(x+1)
  if rem >= 1:
    num = num - rem
    a.append(rem)
  else :
    break

for x in range(len(a)):
  b.append(a[x]/(10**(x)))
num = 0
for x in range(len(a)):
  num = num + (b[x]*10**(len(a)-1-x))

print "Reversed number: %d" %num
