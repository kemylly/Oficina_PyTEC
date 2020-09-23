print('Calculadora\n')

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o primeiro numero: '))

print('\nDigite o numero que deseja fazer a operação')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisao')
resposta = int(input())

if resposta == 1:
    resposta = num1 + num2
    print(num1, ' + ', num2, ' = ', resposta)
else:
    if resposta == 2:
        resposta = num1 - num2
        print(num1, ' - ', num2, ' = ', resposta)
    else:
        if resposta == 3:
            resposta = num1 * num2
            print(num1, ' * ', num2, ' = ', resposta)
        else:
            if resposta == 4:
                resposta = num1 / num2
                print(num1, ' / ', num2, ' = ', resposta)
            else:
                print('Voce digitoou um valor invalido')