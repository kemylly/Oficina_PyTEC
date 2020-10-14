#Calculo de uma multa de velocidade de transito
#Se ultrapassar 70km será multado
#A multa é de 10 reais para cada km acima do permitido (70km)

velocidade = int(input('Digite a velocidade que estava o carro: '))

if velocidade > 70:
    multa = (velocidade - 70)*10
    print('Você foi multado')
    print('Devera pagar: ',multa)
    
else:
    print('Parabens, voce estava dentro do limite permitido')