r = 1
b = 2
e = 9
d = 7
s = 3
for i in range(2,60):
 # Need to generate new range
 if i == e:
   b = e + 1
   d += 8
   e = b + d
   r += 1
   s += 2
 # Perform actions
 else:
   if i == 368078:
     print r, "begining:",b , i-b, s
     
