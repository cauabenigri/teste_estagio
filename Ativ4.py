faturamento_estados = [["SP", 67.836,43], ["RJ", 36.678,66], ["MG", 29.229,88], ["ES", 27.165,48], ["Outros", 19.849,53]]
faturamento_estados_percentual = [["SP", 0], ["RJ", 0], ["MG", 0], ["ES", 0], ["Outros", 0]]

total = 0

for estado in range(len(faturamento_estados)):
    total += faturamento_estados[estado][1]

for estado in range(len(faturamento_estados)):
    faturamento_estados_percentual[estado][1] = faturamento_estados[estado][1]*100/total

for estado in range(len(faturamento_estados_percentual)):
    if faturamento_estados_percentual[estado][0] == "Outros":
        print(f"{faturamento_estados_percentual[estado][0]} participam com {faturamento_estados_percentual[estado][1]}% de faturamento")
    else:
        print(f"{faturamento_estados_percentual[estado][0]} participa com {faturamento_estados_percentual[estado][1]}% de faturamento")
