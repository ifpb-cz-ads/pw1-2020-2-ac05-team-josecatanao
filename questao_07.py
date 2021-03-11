L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
v=int(input("Digite o valor a procurar:"))
x=0
posiP=999
posiV=999

while x<len(L):
  if L[x]==p:
    posiP=x
  if L[x]==v:
    posiV=x
  x+=1

if posiP==999 and posiV==999 :
  print("Nenhum dos dois foi encontrado")

if posiP==999:
  print(p,"não foi encontrado")
else:
  print(p,"foi encontrado na posição:",posiP)

if posiV==999:
  print(v,"não foi encontrado")
else:
  print(v,"foi encontrado na posição:",posiV)