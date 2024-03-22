import math

def calcular_tinta(area):
    # Calcula a quantidade de litros necessários para pintar uma parede.
    litros = area / 6
    litros_com_folga = litros * 1.1

    # Calcula a quantidade de latas e galões
    latas = math.ceil(litros_com_folga / 18)
    galoes = math.ceil(litros_com_folga / 3.6)

    # Calcula o preço
    preco_latas = latas * 80
    preco_galoes = galoes * 25

    latas_mistura = latas
    galoes_mistura = galoes
    while(latas_mistura * 18) - litros_com_folga > 3.6:
        latas_mistura -= 1
        galoes_mistura += 1

    preco_mistura = (latas_mistura * 80) + (galoes * 25)

    return {
        "litros_tinta": litros_com_folga,
        "latas": latas,
        "galoes": galoes,
        "preco_latas": preco_latas,
        "preco_galoes": preco_galoes,
        "latas_mistura": latas_mistura,
        "galoes_mistura": galoes_mistura,
        "preco_mistura": preco_mistura
        }

area = float(input("Digite a área em m^2 que deverá ser pintada: "))

resultado = calcular_tinta(area)

print("Sera preciso {:.2f} litros de tinta".format(resultado["litros_tinta"]))
print("Caso for comprar apenas latas de 18 litros, sera necessário {} latas de tinta, e custara R${:.2f}".format(resultado["latas"], resultado["preco_latas"]))
print("Caso for comprar apenas galões de 3.6 litros, sera necessário {} galões de tinta, e custara R${:.2f}".format(resultado["galoes"], resultado["preco_galoes"]))
print("Caso for comprar a mistura de cada produto sera preciso de {} latas de tinta, {} galões de tinta, e ao todo custara R${:.2f}".
      format(resultado["latas_mistura"], resultado["galoes_mistura"], resultado["preco_mistura"]))