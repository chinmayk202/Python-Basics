num =int(raw_input("Enter length of array: "))
list = []
for x in range(num):
  list.append(raw_input("Enter element: "))
print "Your array: ",
for x in range(num):
  print list[x],
