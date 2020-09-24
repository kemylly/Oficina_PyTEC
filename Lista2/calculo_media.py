#utilizando maior que 6 aprovado
#entre 4 e 6 recuperacao
#menor que 4 reprovado

print('Calculo da media aritmetica de 4 notas\n')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = float

media = nota1 + nota2 + nota3 + nota4
media = media / 4

print('\nA media aritmetica das notas são = ', media)

if media > 6:
    print('Aprovado')
else:
    if media > 3 and media < 7:
        print('Recuperacao')
    else:
        if media < 4:
            print('Reprovado')
        else:
            print('Erro')
            
            
            
            
            