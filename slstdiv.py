from math import sqrt

n =int(raw_input("Enter number to get smallest divisor: "))
d = 3
r = sqrt(n)
if n%2 == 0:
  print "Smallest divisor = 2"
else:
  while n%d != 0 and d< r:
    d = d+2

  if n%d == 0:
    print "Smallest divisor = %d" %d

  else :
    print "Prime number..."
