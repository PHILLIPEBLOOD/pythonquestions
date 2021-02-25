'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''


def fibo(valor1, valor2, quantidade):
    if(quantidade == 0):
        return ""
    return str(valor2) + ", " + fibo(valor2, valor1 + valor2, quantidade - 1)


quantidade = int(input("Contagem final da fibo: "))
fibonacci = fibo(0, 1, quantidade)
final = len(fibonacci) - 2
print(fibonacci[0:final])
