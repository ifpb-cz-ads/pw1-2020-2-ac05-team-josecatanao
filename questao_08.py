T = [ -10, -8, 0, 1, 2, 5,10, -2, -4,-11]
menor=T[1]
maior=T[1]

for n1 in T:
  if n1<menor:
    menor=n1
  if maior<n1:
    maior=n1

print("A menor temperatura é:",menor)
print("A maior temperatura é:",maior)
print("a media das temperaturas é:",sum(T)/len(T))