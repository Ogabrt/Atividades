nome = str(input("Digite seu nome: "))
xp = int(input("Qual a sua Xp ?: "))
if xp <= 1000:
    print("O heroi de nome {} está no nivel de Ferro".format(nome))
elif xp >1000 and xp <= 2000:
    print("O heroi de nome {} está no nivel de Bronze".format(nome))
elif xp >2000 and xp <= 5000:
    print("O heroi de nome {} está no nivel de Prata".format(nome))
elif xp >6001 and xp <= 7000:
    print("O heroi de nome {} está no nivel de Ouro".format(nome))
elif xp >7001 and xp <= 8000:
    print("O heroi de nome {} está no nivel de Platina".format(nome))
elif xp >8000 and xp <= 9000:
    print("O heroi de nome {} está no nivel de Ascendente".format(nome))
elif xp >9000 and xp <= 1000:
    print("O heroi de nome {} está no nivel de Imortal".format(nome))
else:
    print("O heroi de nome {} está no nivel de Radiante".format(nome))   