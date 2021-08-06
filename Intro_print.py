# print("Hello World!")
# # print("`^`P^Ç`^Ç^Ç´qa~A^Sd?Â!@##$#$%$%¨%&*&*(&%$//'''''")
# # print é a função para escrever na saida.
# print('''primeira linha
# segunda linha
#     hello
# ..
# ''')
# print("algo\talgo\balgo\nalgo\'algos\"algo\\")
# \b é o backspace
# \t é tab
# \n new line

qualquer_nome = 'hello'
y12 = 'world'

# print("Tradição do:", qualquer_nome, y12, sep='-')  # sep vai modificar como separa as variáveis
# print("Tradição do" + " " + qualquer_nome + " " + y12)  # TEM QUE SER STRING
# print("Tradição do %s %s" % (qualquer_nome, y12))
# print(f"Tradição do {qualquer_nome} {y12}")

# print("Primeira linha", end='\t')  # end='' modifica o final do print
# print("continuação da primeira linha")

# integeter int representaçao do conjunto dos Z (inteiros)
# poder_de_luta = 8000
# poder_de_luta += 100  # += é equivalente a  = variável +
# poder_de_luta -= 100
# print(poder_de_luta, type(poder_de_luta))
# # str() transforma a variável para string
# # print("O poder de luta dele é mais de" + str(poder_de_luta))  # TypeError
# poder_de_luta *= 2
# poder_de_luta /= 1
# print(poder_de_luta, type(poder_de_luta))
# print("O poder de luta dele é mais de", poder_de_luta)  # não tem typeerror

# float são variávies do conjunto R (racionais)
# altura = 250.5
# print(altura, type(altura))
# altura -= 88.3
# print(f"A sua altura é {altura}cm")
# print("A sua altura é %.1fcm" % (altura))

# Boolean: São variáveis binarias que guardam apenas True ou False
# human = True
# print(human, type(human))
# print("O pc é humano?", human)

# Type Casting
# y = 2.9
# print('y :', y, type(y))
# y = int(y)  # int() função para converter a variável para integer
# print('y :', y, type(y))
# y = str(y)
# print('y : ' + y, type(y))
# # print(y*3)  # repetir a string 3 vezes
# y = float(y)
# print('y :', y, type(y))
# y = False
# print('y :', y, type(y))
# y = None
# print('y :', y, type(y))

# multiple Assignments

# x = y = z = w = r = t = None
# print(x, y, z, w, r, t)
#
# y, human, poder_de_luta, palavra = 2.9, False, 8000, "olá"
# print(y, human, poder_de_luta, palavra)
# print(type(y), type(human), type(poder_de_luta), type(palavra))