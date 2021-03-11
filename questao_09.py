
palavra = input("Digite a palavra:")
dicionario = []

for letra in palavra:
  valor = letra,":",palavra.count(letra)
  dicionario.append(valor)  
lista=set(dicionario)

for letra in lista:
  print(letra)




