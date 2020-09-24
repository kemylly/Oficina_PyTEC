#Elabore um programa que solicite ao usuário a distância de uma
#viagem em Km. Calcule o preço da passagem, cobrando R$
#0.20 por Km para viagens de até 100 km e R$ 0.15 para viagens
#mais longas.

print('Calculo do preco da passagem')
distancia = float(input('Digite a distancia da viagem em km: '))

if distancia < 101:
    passagem = distancia * 0.20
    print('O preco da passagem fica =', passagem, 'reais')
else:
    if distancia > 100:
        passagem = distancia * 0.15
        print('O preco da passagem fica =', passagem, 'reais')
    else:
        print('Erro')
