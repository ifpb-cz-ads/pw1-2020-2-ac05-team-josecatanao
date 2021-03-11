lista1=['(','(',')',')']
aberta=0
fechada=0
for n in lista1:
  if n =='(':
    aberta+=1
  if n ==')':
    fechada+=1
if aberta==fechada:
  print('ok')
else:
  print('erro')

#***************************************************

lista1=['(',')','(',')','(','(',')','(',')',')' ]
aberta=0
fechada=0
for n in lista1:
  if n =='(':
    aberta+=1
  if n ==')':
    fechada+=1
if aberta ==fechada:
  print('ok')
else:
  print('erro')

#***************************************************
  
lista1=['(',')',')']
aberta=0
fechada=0
for n in lista1:
  if n =='(':
    aberta+=1
  if n ==')':
    fechada+=1
if aberta==fechada:
  print('ok')
else:
  print('erro')



