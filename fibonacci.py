num = int(raw_input("Enter the number of numbers you want: "))

term = 1
pterm = 0
list = [0,1]

for x in range(num):
  term = term + pterm
  pterm = term - pterm
  list.append(term)

for x in range(num):
  print list[x],
