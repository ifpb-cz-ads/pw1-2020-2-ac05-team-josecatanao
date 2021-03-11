lista1 =[]
lista2 =[]
lista3 =[]
cont=1

while cont<=3:
  nu=input('Digite um numero')
  lista1.append(nu)
  cont+=1

cont=1

while cont<=3:
  nu=input('Digite um numero')
  lista2.append(nu)
  cont+=1

lista3.append(lista1)
lista3.append(lista2)

for n in lista3:
  print(n)


