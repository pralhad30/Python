X = [('Tom',19,80),('John',20,90),('
Jony',17,91),('
Jony',17,93),('
Json',21,85)]
Y = sorted(X,key=lamda tup:(tup[0],tup[1],tup[2]))

print Y
