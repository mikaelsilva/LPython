a=1
b=1
c=a+b
d='Mikael Vidal'
e='Sr. '

#TESTANDO O GIT


#Strings - Valores nao podem variar de tipo
print '1 -> ',c,d
print '2 -> ',c,d[::-1]
print e + d
print len(d),'\n\n\n\n'


#Lista - Valores podem variar de tipo
lista=[1,1,1,4.12345]
lista2=['Tchau',3,'Inimigo',-4.12345]
print lista[0]+lista[2],lista[1]
lista=lista+['Ultimo valor']
print lista
print len(lista)
lista=lista+[10]
print 'A lista possui um novo valor',len(lista)
matriz=[lista,lista2]
print matriz
print matriz[1][0],'and tam matriz',len(matriz)

lista.append('NovoValorAdicionado')#inclui no final da lista
print lista,'\n'
lista.extend(['1',1,3,4,101])
lista.insert(0,'PosZeroNovoValor')
print lista,'\n'
lista.remove('NovoValorAdicionado')
print lista,'\n'
lista.pop(0)
numero1=lista.count(1)
print '\n\n\n',numero1,'\n\n\n'
print lista,'\n\n\n\n'


#Tuplas - Valores nao podem variar de tipo
#Utilizadas para serem chaves de Dicionarios
tupla=(1,2,3,4,5)
print tupla,'\n\n\n\n'


#Dicionarios - Sao mutaveis
#Seus valores sao encontrados a partir de 
#chaves, e nao por posiocionamento
dicionario={'chave1':'PrimeiraPortaAberta','chave2':'SegundaPortaAberta'}

print dicionario
print dicionario['chave1']
dicionario['chave3']='TerceiraPortaAberta'
print '**Solicitacao para armazamento de nova chave','\n',dicionario
print dicionario['chave2'],'\n',dicionario['chave3']

print dicionario.keys()#Retorna todas as chaves existentes no dicionario
print dicionario.has_key('chave1')#verifica se a chave existe,retorna False ou True
print dicionario.has_key('chave4')
print dicionario.items() #retorna uma tupla do dicionario, relacionando a chave e seu valor atribuido
print '\n\n\n\n'

#Formatando String
num=17
num2=2.11231
num3='Mikael'
print 'Meu nome eh numero %d' %num
print 'Meu nome eh numero %2.2f'%num2
print 'Meu nome eh numero %s' %num3
print '%s Meu nome eh numero %s' %(num3,num3)
print '\n\n\n\n'


#Condicional
#var1=int(raw_input('Insira valor para permissao: '))
var1=10
if var1 < 17:
	print 'Voce nao esta autorizado para dirigir\n'
elif var1 == 17:
	print 'Voce ja esta autorizado para TIRAR A CARTEIRA DE MOTORISTA'
else:
	print 'Voce esta autorizado para dirigir\n'


#LOOPS

#WHILE
#varWhile = int(raw_input('Insira o valor para analise: ')) #leitura de teclado
varWhile=1
varWhile2=varWhile+10
while varWhile <= varWhile2:
	print varWhile
	varWhile=varWhile+1
	varWhile-=1
	varWhile+=1

print 'Terminou a condicao de %d' %(varWhile),'\n\n\n\n'

#FOR
varFor = 10
a= {'Mikael','Vidal','da','Silva'}

for x in range(varFor): # ou for x in a 
	print '%d' %(x)
print 'Fim do FOR\n'

for x in range(10):
	print '%d' %x, #A virgula permite imprimir os elementos na mesma linha durante o for
print '\n'

for x in dicionario:
	print 'A chave %s eh dada por X do for'%x
	print 'O valor das chaves eh dado por dicionario[x]: %s'%dicionario[x]


for y in range(2,5):
	if 3 % y == 0: 
		break
	else:
		print 'O numero e impar'
print 'Fim do programa'


#TRATANDO ERROS (TRY e EXCEPT)
print 'TENTE ISSO:'
lst=[12]

while 1:
	try:
		#lst.append(int(raw_input('Digite um valor:')))
		print lst
		#if len(lst)==5:
		break
	except:
		print 'Voce informou um valor incorreto!!'
		print lst 



#FUNCOES E MODULOS
print '\n\nFUNCOES'
def func_derivada(tupla2,*argumento):
	soma=0
	soma2=0

	print 'Derivada realizada com sucesso '

	for i in tupla2:
		print 'Valor da tupla posicao '
		soma+=i

	for i in argumento:
		print 'Valor dos argumentos '
		soma2+=i
	print soma
	print soma2
	
	return soma,soma2

print 'PULOU A FUNCAO'

tupla2=(1,10,20,30)

print 'Chamando a funcao'

var1,var2=func_derivada(tupla2,12,3,1,2,3)
print 'Deu certo tupla: %d E Deu certo argumentos %d' %(var1,var2)


#def main
#main()


print 'FUNCOES 2'

def printar(valores):
	print valores


argumentos=[1,2,3,4,5,6,7,8,9,10]
map (printar,argumentos)

PAG 59








