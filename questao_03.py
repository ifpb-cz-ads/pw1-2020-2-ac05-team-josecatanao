lista1=[1,2,3,4]
lista2=[2,8,6,9]
lista3=[]

for n1 in lista1:
  lista3.append(n1)


for n1 in lista2:
    if n1 not in lista3:
        lista3.append(n1)

for n in lista3:
  print(n)