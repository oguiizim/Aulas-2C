import math

mb = float(input("Digite o tamanho do arquivo em mB: "))
mbps = float(input("Digite a velocidade  de download em MB/s: "))

mbpm = mbps * 60

timeSeg = math.ceil(mb / mbps)
timeMin = math.ceil(mb / mbpm)

print("O tempo aproximado de download será de {} segundos ou {} minutos.".format(timeSeg, timeMin))
