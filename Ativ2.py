# Váriáveis definidas
fibnum1anterior, fibnum2anterior = 1, 0
fibnum = 0

# Pergunta ao usuário o número à ser pesquisado
numero = int(input('Informe um numero: '))

# Percorre a sequência de fibonacci
while True:
    # Se o número for o da vez, o anterior ou anterior ao anterior, o script responde que há.
    if numero == fibnum or numero == fibnum1anterior or numero == fibnum2anterior:
        print(f'O numero {numero} se encontra na lista.')
        break

    # Progride uma casa na sequência
    elif numero > fibnum:
        fibnum = fibnum1anterior + fibnum2anterior
        fibnum2anterior = fibnum1anterior
        fibnum1anterior = fibnum

    # Se o número não for o da vez, não for o anterior e nem o anterior ao anterior, o script responde que não há.
    elif numero != fibnum and numero < fibnum:
        print(f'O numero {numero} não se encontra na lista.')
        break
