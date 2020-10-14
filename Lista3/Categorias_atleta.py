#Calcula em qual categooria um atleta está com base no seu ano de nascimento
#Categorias:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 25 anos: SÊNIOR
#Acima: MASTER

print('Descubra a categoria do atleta\n')
ano = int(input('Digite o ano de nascimento do atleta: '))

categoria = 2020 - ano

if categoria <= 9:
    print('Mirim')
else:  
    if categoria <=14:
        print('Infantil')
    else:
        if categoria <= 19:
            print('Junior')
        else:
            if categoria <= 25:
                print('Senior')
            else:
                print('Master')