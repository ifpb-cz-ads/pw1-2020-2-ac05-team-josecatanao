L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
v=int(input("Digite o valor a procurar:"))
x=0
while x<len(L):
  if L[x]==p:
    print("%d foi achado priemiro na posição %d" % (p,x))
    break
  if L[x]==v:
    print("%d foi achado priemiro na posição %d" % (v,x))
    break
  x+=1
if x == len(L):
  print("Não foi encontrado nem um dos dois")