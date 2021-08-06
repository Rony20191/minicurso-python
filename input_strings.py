# input(__prompt__)
# A FUNÇÃO INPUT SEMPRE RETORNA UMA STRING
# int() float()
# nome = input("Qual o seu nome: ")
# print("Hello, " + nome)
# print("O Seu nome tem", len(nome), "caracteres, com os espaços")  # len(variável) retorna int do tamanho da string
# print("A posição do caractere e é:", nome.find('e'))
#     # Computador SEMPRE COMEÇA DO 0
#     # string.find('char') é a função que retorna um int da posição do caractere
#     # sempre vai retornar o primeiro char que achar
#     # retornar -1 caso não tenha algo igual
# print(nome.capitalize())  # o primeiro char fica maiúsculo
# print(nome.title())  # o primeiro char de todas as palavras ficam maiúsculo
# print(f"{nome.lower()} normalmente, mas {nome.upper()} quando pisa na bola")
    # .lower faz a string toda ficar minuscula
    # .upper faz a string ficar toda maiúscula
# print(nome.isalpha())  # retorna true se a string tiver apenas char alfabético
# print(nome.isdigit())  # retornar true se a string tiver apenas char numérico
# print("O seu nome tem", nome.count('a'), "as")  # string.count('char')
# print("O seu nome tem", nome.count('A'), "As")  # string.count('char')
    # .count() retorna um int de quantas vezes o char aparece na string
    # CASE SENSITIVE
# print("O seu nome tem", nome.lower().count('a'), "A's")  # string.count('char')
# print("Eu prefiro 'e' à 'a', então seu nome agora é", nome.lower().replace('a', 'e').title())
    # string.replace('old_char', 'new_char')
    # retornar uma string nova trocando o char antigo pelo char novo
    # Case Sensitive

# altura = float(input("Qual a sua altura? "))
# altura = int(altura)
# print(f"Sua altura é {altura} do tipo {type(altura)}")

nome = 'Ana Atala'
    #   0123456789
# Slicing: uma sub-string extraindo elementos de uma outra string
        # index[]  começo:fim:incremento
        # começo é inclusivo
        # fim é exclusivo

print(nome[1])  # retornar um char da sua string
print(nome[0:2])  # an
print(nome[0:3])  # ana
print(nome[:3])  # ana
print(nome[3:])  #  atala
print(nome[::2])  # o step ele muda o incremento
print(nome[::-1])  # o step ele muda o incremento

