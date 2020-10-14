#Digite um valor qualquer e será calculada sua tabuada do 1 ao 10
#resolvido com while

print('Calculo da tabuada')

num1 = int (input('Digite um valor: '))

num2 = 1
while (num2 < 11):
    resp = num1 * num2
    print(num1,' * ',num2,' = ',resp)
    num2 = num2 + 1
