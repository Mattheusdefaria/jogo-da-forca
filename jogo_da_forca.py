import os
os.system('cls')

palavra = 'celular'
lista_letras = []
letras_digitadas = []
nova_palavra = '*'*len(palavra)
contagem = 6

print('Bem Vindo Ao Jogo Da Forca')

while True:
    letra = input('Digite uma letra: ')
    letra = letra.lower()
    if letra not in 'abcdefghijklmnopqrstuvwxyz':
        print('-'*66)
        print('Entrada Invalida - Não é permitido números ou caracteres especiais')
        print(f'A palavra está assim {nova_palavra}')
        continue
    elif letra == '':
        print('-'*36)
        print('Entrada Invalida - Escreva uma letra')
        print(f'A palavra está assim {nova_palavra}')
        continue
    elif letra in lista_letras or letra in letras_digitadas:
        print('-'*33)
        print('Entrada Invalida - Letra repetida')
        print(f'Letras já digitadas: {letras_digitadas}')
        print(f'A palavra está assim {nova_palavra}')

        continue
    else:
        lista_letras.append(letra)
        letras_digitadas.append(letra)
        if letra in palavra:
            print()
            print('_' * 30)
            print(f'A letra "{letra}" existe na palavra')
        else:
            contagem -= 1
            print('_' * 30)
            print()
            print(f'A letra "{letra}" não existe na palavra')
            lista_letras.pop()

    nova_palavra = ''

    for l in palavra:
        if l in lista_letras:
            nova_palavra += l
      
        else:
            nova_palavra += '*'

    print(f'A palavra está assim {nova_palavra}')
    print(f'Letras já digitadas: {letras_digitadas}')
    print(f'Você ainda tem {contagem} chances !')

    if contagem == 0:
        print(f'Você perdeu o jogo')
        print(f'A palavra era "{palavra}"')
        break
    if nova_palavra == palavra:
        print('Você ganhou o jogo !')
        print(f'A palavra era "{palavra}"')
        break