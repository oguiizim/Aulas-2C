gender = int(input("Feminino - 1\nMasculino - 2\nQual seu gênero: "))
height = float(input("Qual sua altura em metros: "))

if(gender == 1):
    calculation = (62.1 * height) - 44.7
    print("Seu peso ideal é {:.2f} kg".format(calculation))
else:
    calculation = (72.7 * height) - 58
    print("Seu peso ideal é {:.2f} kg".format(calculation))