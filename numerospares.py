print('Algoritimo que imprime todos numeros pares entre 1 e o numero fornecido pelo usuario!','\n')

numero = input('\n Digite o Numero:')
numero = int(numero)

par = 1

for par in range(par,numero+1):
    if par % 2 ==0:
        
        print('\n Este numero e par:',par,'\n')
