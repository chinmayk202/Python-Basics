n = float(raw_input("Enter the number to get square root: "))
g1 = n/2
g2 = 2.0

while abs(g1-g2)>0.00001 :
  g2 = g1
  g1 = (g1 + n/g1)/2

print "Square root of %f = %f" %(n,g1)
