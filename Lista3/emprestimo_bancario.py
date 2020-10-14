#Aprovar um emprestimo bancario para a compra de uma casa

casa = float(input('Digite o preço da casa: '))
salario = float(input('Digite o salario do comprador: '))
anos = float(input('Digite o numero de anos que será pago: '))

#verificar quantos meses será pago
meses = anos * 12

#calcular quanto ficara a mensalidade para pagar a casa
mensalidades = casa / meses

#Calcular o valor maximo permitido para descontar do salario (40%)
maximo = (salario*40) / 100

if mensalidades > maximo:
    print('Emprestimo negado')
else:
     print('Emprestimo permitido')