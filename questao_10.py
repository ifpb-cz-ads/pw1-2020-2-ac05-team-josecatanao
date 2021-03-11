estoque={ "tomate": [ 1000, 2.30], "alface": [ 500, 0.45], "batata": [ 2001, 1.20], "feijão": [ 100, 1.50] }
total = 0
print("Vendas:\n")
print('Digite um valor para realizar a compra')
print('1->tomate')
print('2->batata')
print('3->alface')
print('*********************')
produto = int(input('Digite o numero:'))
quantidade = int(input('Digite o numero:'))

if produto==1:
  venda = [["tomate", quantidade]]
elif produto ==2:
  venda = [["batata", quantidade]]
elif produto ==3:
   venda = [["alface", quantidade]]

for operação in venda:
	produto, quantidade = operação
	preço = estoque[produto][1]
	custo = preço * quantidade
	print("%12s: %3d x %6.2f = %6.2f" %
(produto, quantidade,preço,custo))	 
	estoque[produto][0] -= quantidade
	total+=custo
    
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")

for chave, dados in estoque.items():
	print("Descrição: ", chave)
	print("Quantidade: ", dados[0])
	print("Preço: %6.2f\n" % dados[1])
