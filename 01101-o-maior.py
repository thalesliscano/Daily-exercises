'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
(a+b + abs(a-b) / 2)
Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
Entrada

O arquivo de entrada contém três valores inteiros.
Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''
a, b, c = map(int, input().split())

# Encontrar o maior número entre a e b
maiorAB = (a + b + abs(a - b)) // 2

# Encontrar o maior número entre o maiorAB e c
maiorFinal = (maiorAB + c + abs(maiorAB - c)) // 2

# Imprimir o resultado no formato correto
print(f"{maiorFinal} eh o maior")
