r = float(raw_input("Enter the number: "))
ans = 0.0
ans = r
r2 = r*r
for x in range(3,5000,2):
  r = -r*r2/(x*(x-1))
  ans = ans + r
print "Sin(%f) = %f" %(r,ans)
