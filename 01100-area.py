'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada

O arquivo de entrada contém três valores com um dígito após o ponto decimal.
Saída

O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
'''
a,b,c = map(float,input().split(" "))
PI = 3.14159

area_triangulo = (a * c) / 2
area_circulo = c ** 2  * PI
area_trapezio = ((a + b) * c) / 2
area_quadrado = b ** 2  
area_retangulo = b * a  

print(f"TRIANGULO: {area_triangulo:.3f}\nCIRCULO: {area_circulo:.3f}\nTRAPEZIO: {area_trapezio:.3f}\nQUADRADO: {area_quadrado:.3f}\nRETANGULO: {area_retangulo:.3f}")