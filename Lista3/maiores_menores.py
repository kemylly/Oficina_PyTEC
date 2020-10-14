#mostrar qual numero é maior e qual é o menor dos digitados

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

#maior
if num1 > num2:
    if num1 > num3:
        print('maior: ',num1)
    else:
        if num3 > num2:
            print('maior: ',num3)
else:
    if num2 > num3:
        print('maior: ',num2)
    else:
        print('maior: ',num3)

#menor
if num1 < num2:
    if num1 < num3:
        print('menor: ',num1)
    else:
        if num3 < num2:
            print('mmenor: ',num3)
else:
    if num2 < num3:
        print('menor: ',num2)
    else:
        print('menor: ',num3)
