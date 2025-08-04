'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
'''

sequencia_de_fibonacci = [1, 1]
while sequencia_de_fibonacci[-1] <= 500:
    valor_sequencia = sequencia_de_fibonacci[-1] + sequencia_de_fibonacci[-2]
    sequencia_de_fibonacci.append(valor_sequencia)
print(sequencia_de_fibonacci)


