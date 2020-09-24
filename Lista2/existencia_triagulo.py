#Faça um programa que receba o comprimento de três retas e
#informe ao usuário se elas podem ou não formar um
#triângulo.(Obs.: Para saber se a forma criada é um triangulo ou
#não utilizamos de sua condição de existência, que é: a medida
#de qualquer um dos lados deve ser menor que a soma das
#medidas dos outros dois e maior que o valor absoluto da
#diferença entre essas medidas.)

ladoa = int(input('Digite o valor do lado A: '))
ladob = int(input('Digite o valor do lado B: '))
ladoc = int(input('Digite o valor do lado C: '))

lado = ladoa + ladob

if lado < ladoc:
    print('Isso não é um triangulo')
else:
    lado = ladoa + ladoc
    if lado < ladob:
        print('Isso não é um triangulo')
    else:
        lado = ladob + ladoc
        if lado < ladoa:
            print('Isso não é um triangulo')
        else:
            print('Isso é um triagulo')
