import time
# if é estrutura de tomada de decisão
# é um bloco de código só vai ser executado se a condição for VERDADEIRA
# else if, elif é um bloco de código que só vai ser executado se a condição do if for falsa
    # e a condição do elif for verdadeira
# else é um bloco de código que so vai ser executado se a condição do if for FALSA

# idade = int(input("Qual a sua idade? "))
#
# if idade >= 100:
#     print("Come essa torta de alho por favor.")
# elif idade >= 18:
#     print("Bora num rolé")
# elif 16 < idade < 18:
#     print("Chegando la")
# else:
#     print("A programação é anime")

# Loop são blocos de código que se repetem enquanto uma condição for verdadeira
# infinite loop: Um bloco de repetição que a condição é sempre verdadeira
# While é um bloco com verificação no começo e ira repetir enquanto essa condição continuar verdadeira
# break é um comando que quando é chamado, ele sai do loop
# For é um bloco de código que repete uma quantidade PREDETERMINADA de vezes


# while 1 == 1:
#     print("SOS. To preso no loop")

# loop para garantir input do usuário
# nome = ""
# while len(nome) == 0 or nome.isdigit():
#     nome = input("escreva o seu nome: ")
# print("hello " + nome)

# mesma funcionalidade de cima, usando break
# while True:
#     nome = input("Escreva o seu nome: ")
#     if nome != "":
#         break
# print("hello", nome)

# for i in range(10):  # incremento. loop foi rodado exatamente 10 vezes
#     print(i+1)        # começou em 0

# for i in nome:  # o i fica com o valor de cada index em nome
#     print(i)

# print("wait for it")
# for seconds in range(10, 0, -1):  # range(começo, fim, incremento)
#     print(seconds)
#     time.sleep(1)   # função sleep do pacote time
# print("GO!")

# Exemplo 'matrizes'
while True:
    linhas = int(input("quantas linhas? "))
    colunas = int(input("quantas colunas? "))
    char = input("Qual char usaremos? ")
    for i in range(linhas):
        for j in range(colunas):
            # O loop de dentro é executado por completo antes de terminar um loop do loop de fora
            print(char, end=" ")  # para nao pular uma linha no loop de dentro
        print()  # para ter uma new line
    if input("Deseja sair do loop? (s/n): ").lower() != 'n':
        break
print("Saímos do loop")
