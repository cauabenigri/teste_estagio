from xml.dom import minidom as md

dias_uteis = 0

dias = []
valores = []

maior_fat, maior_dia = 0,0
menor_fat, menor_dia = 0,0

media = 0

dias_acima_da_media = 0

with open("dados.xml", 'r', encoding='utf-8') as file:
    xml = md.parse(file)
    dia_tag = xml.getElementsByTagName("dia")
    valor_tag = xml.getElementsByTagName("valor")
    for tag in dia_tag:
        dias.append(tag.firstChild.data)
    for tag in valor_tag:
        valores.append(tag.firstChild.data)

for v in range(len(valores)):
    if float(valores[v]) > maior_fat:
        maior_fat = menor_fat = float(valores[v])
        maior_dia = v + 1

for v in range(len(valores)):
    if float(valores[v]) != 0:
        if float(valores[v]) < menor_fat:
            menor_fat = float(valores[v])
            menor_dia = v + 1
        dias_uteis += 1
        media += float(valores[v])


media = media / dias_uteis
for v in valores:
    if float(v) > media:
        dias_acima_da_media += 1

print(f'O maior faturamento foi no dia {maior_dia}, com R${maior_fat}')
print(f'O menor faturamento foi no dia {menor_dia}, com R${menor_fat}')
print(f'Neste mês houveram {dias_acima_da_media} dias acima da média')
