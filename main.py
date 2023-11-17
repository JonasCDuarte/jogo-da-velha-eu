from random import randint
a = 0
cont = 0
global lista

lista = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

jogador = False

def tela():
    print('       0      1      2')
    print(f'0 -    {lista[0][0]}   |   {lista[0][1]}   |   {lista[0][2]}')
    print('     ------------------')
    print(f'1 -    {lista[1][0]}   |   {lista[1][1]}   |   {lista[1][2]}')
    print('     ------------------')
    print(f'2 -    {lista[2][0]}   |   {lista[2][1]}   |   {lista[2][2]}')


while True:
    if jogador == False:
        while True:
            if lista[0][0] == 'X' and lista[0][1] == 'X' and lista[0][2] == 'X' or lista[1][0] == 'X' and lista[1][1] == 'X' and lista[1][2] == 'X' or lista[2][0] == 'X' and lista[2][1] == 'X' and lista[2][2] == 'X' or lista[0][0] == 'X' and lista[1][1] == 'X' and lista[2][2] == 'X' or lista[2][0] == 'X' and lista[1][1] == 'X' and lista[0][2] == 'X' or lista[0][0] == 'X' and lista[1][0] == 'X' and lista[2][0] == 'X' or lista[0][1] == 'X' and lista[1][1] == 'X' and lista[2][1] == 'X' or lista[0][2] == 'X' and lista[1][2] == 'X' and lista[2][2] == 'X':
                tela()
                jogador = True
                print('Jogador 1 venceu!')

                break
            else:
                tela()
                l = int(input('Qual linha deseja tirar: '))
                c = int(input('Qual coluna deseja tirar: '))
                cont += 1

                if l < 3 and c < 3:
                    if len(lista[l][c]) == 0:
                        lista[l][c] = 'X'
                        break
                    else:
                        print('Esta célula já está ocupada.')
                else:
                    print('O valor digitado é maior que o permitido! ')

        while True:
            if lista[0][0] == 'O' and lista[0][1] == 'O' and lista[0][2] == 'O' or lista[1][0] == 'O' and lista[1][1] == 'O' and lista[1][2] == 'O' or lista[2][0] == 'O' and lista[2][1] == 'O' and lista[2][2] == 'O' or lista[0][0] == 'O' and lista[1][1] == 'O' and lista[2][2] == 'O' or lista[2][0] == 'O' and lista[1][1] == 'O' and lista[0][2] == 'O' or lista[0][0] == 'O' and lista[1][0] == 'O' and lista[2][0] == 'O' or lista[0][1] == 'O' and lista[1][1] == 'O' and lista[2][1] == 'O' or lista[0][2] == 'O' and lista[1][2] == 'O' and lista[2][2] == 'O':
                tela()
                jogador = True
                print('Jogador 2 venceu!')
                break
            else:
                l = randint(0, 2)
                c = randint(0, 2)
                cont += 1

                if len(lista[l][c]) == 0 and a == 0:
                    lista[l][c] = 'O'
                    break


    else:
        print('Programa finalizado! ')
        break
