import random
# lists = utilizada para armazenar multiplos items em uma unica variavel.

# bebidas = "terere"
# print(bebidas)

bebidas = ["terere", "coca", "cha", "cafe"]
numeros = [1123, 312, 12, 1, -1]
print(bebidas)
# print('primeiro elemento: ' + bebidas[0])
# print('segundo elemento: ' + bebidas[1])
# # print("quarto elemento: " + bebidas[4]) # IndexError: list index out of range
# bebidas[0] = "chimarrão"
# print('primeiro elemento: ' + bebidas[0])
# print(bebidas[-1])  # ordem inversa
# print(bebidas[1:3])  # o indice do fim é exclusivo
# print(bebidas[:3])
# print(bebidas[2:])

# # imprimindo listas usando for loop
# for i in bebidas:
#     print(i)
# for i in numeros:
#     print(i)

# manipulando listas com métodos
# .clear() apaga todos os elementos da lista
# print(bebidas.clear())  # escreve 'none'
# .count(elemento) conta quantas vezes o elemento aparece  na lista
# .reverse() inverte os elementos da lista
# bebidas.reverse()
# random.shuffle(lista) embaralha a lista de modo aleatorio
# random.shuffle(bebidas) 
# .append acrescenta um elemnto ao fim da lista
# bebidas.append("cerveja")
# .remove remove um elemento da lista
#bebidas.remove("coca")
#bebidas.remove(bebidas[1]) #podemos usar o proprio indice na hr de remover
# .pop remove o ultimo objeto
#bebidas.pop()
# .insert(index,value) ira inserir um valor no index expecificado
# bebidas.insert(0,"milkshake")
# .sort(reverse=True|False, key=myFunc) ira organizar uma lista por ordem alfabetica (reversa ou nao), ou na ordem da função especificada
# bebidas.sort()

# bebidas.upper()  # AttributeError: 'list' object has no attribute 'upper'
# bebidas = [i.upper() for i in bebidas]  # como fazer tudo ficar upper.
# numeros.sort(reverse=True)
# numeros = [i**(1/2) for i in numeros]  #funciona para numeros
# print(type(numeros[4]))  # python trabalha com numeros complexos

# for i in bebidas:
#     print(i)
# for i in numeros:
#     print(i)

# 2d lists: Uma lista de listas
jogos = ['League of legends', 'csgo', 'dark souls', 'minecraft']
plataformas = ['windows', 'xbox', 'ps5', 'nintendo']
game_night = [bebidas, jogos, plataformas]
# print(game_night)
# print(game_night[1])
# print(game_night[1][3])
game_night.append('abacate')
jogos.append('valorant')
game_night.insert(0, ['#', '#'])
# print(game_night)
