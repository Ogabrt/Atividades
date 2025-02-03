vitorias = int(input("quantas vitorias voce teve ?: "))
derrotas = int(input("Qunats derotas voce teve ?: "))
partidas = vitorias - derrotas
if vitorias < 10:
    nivel = "ferro"
elif vitorias <= 20:
    nivel = "Bronze"
elif vitorias <= 50:
    nivel = "Prata"
elif vitorias <= 80:
    nivel = "Ouro"
elif vitorias <= 90:
    nivel = "Diamante"
elif vitorias <= 100:
    nivel = "Lendário"
else:
    nivel = "imortal"    
print("O Herói tem de saldo {} está no nivel de {}".format(vitorias, nivel))
