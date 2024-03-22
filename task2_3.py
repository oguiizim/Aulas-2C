peso_regulador = 50
valor_multa = 4

def excesso(peso_peixe):
    if(peso_peixe > 50):
        excesso = peso_peixe - 50
        return excesso
    else:
        return 0

def multa(excesso):
    multa = excesso * valor_multa
    return multa

peso_peixe = float(input("Digite o peso do peixe pescado: "))

excesso = excesso(peso_peixe)
multa = multa(excesso)

print("Como o peixe pescado tem {} kgs, o seu peso de excesso em kg é: {}".format(peso_peixe, excesso))
print("A sua multa será de: {}".format(multa))