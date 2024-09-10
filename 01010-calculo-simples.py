'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
Entrada

O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
Saída

A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
'''

codigo_peca,numero_peca,valor_peca = input().split(" ")
codigo_peca_2,numero_peca_2,valor_peca_2 = input().split(" ")

codigo_peca = int(codigo_peca)
numero_peca = int(numero_peca)
valor_peca = float(valor_peca)

codigo_peca_2 = int(codigo_peca_2)
numero_peca_2 = int(numero_peca_2)
valor_peca_2 = float(valor_peca_2)

calculo_peca_um = numero_peca * valor_peca
calculo_peca_dois = numero_peca_2 * valor_peca_2
total = calculo_peca_um + calculo_peca_dois
print(f"VALOR A PAGAR: R$ {total:.2f}")