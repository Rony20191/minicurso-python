import math
# - +, * / mod div, sqrt pow, ()

# A, B, C = 3, 5, 10
# print(C * B)  # 50
# print(C / B)  # 2.0
# print(C % A)  # % MOD o resto da divisão
# print(C // A)  # // DIV é o quociente
# print(pow(2, A))  # pow(base, expoente)
# print(2 ** A)   # base ** expoente
# print(math.sqrt(C))  # sqrt da biblioteca math
# print(C ** (1/2))
# print((30 % 4 * (3**3)*(-1)))

# Operadores de comparação retornam True ou False
# > MAIOR QUE
# < MENOR QUE
# >= MAIOR OU IGUAL QUE
# <= MENOR OU IGUAL QUE
# == É IGUAL QUE
# != DIFERENTE DE
A, B, C = 3, 5, 10
# print(B*2 == C)
# print(2 + 8 % 7 >= 3 * 6 - 15)

# Operadores Lógicos
# not NÃO
# and E
# or OU

# print(not(B > C))
# print(A < C and B > C)
# print(A < B < C)
# print(A < C or B > C)

# print((not True) or 20 // (18/3) != (21/3) // 2)
# print(False or 20 // 6 != 7 // 2)

pi = math.pi
print(pi, type(pi))
print("O valor arredondado é:", round(pi)) # round() arrendonda para o int mais prox
print("O valor arredondado para cima é:", math.ceil(pi)) # ceil ceiling int maior mais prox
print("O valor arredondado para baixo é:", math.floor(pi)) # floor chão, int menor mais prox
pi *= -2
print(f"O valor é {pi} e o modulo é {abs(pi)}")  # abs() retorna o modulo do número
pi /= -2
# pow existe pow(base,expoente)
# sqrt existe math.sqrt(numero)
print("O maior valor entre A, B, C é:", max(A, B, C))
print("O menor valor entre A, B, C é:", min(A, B, C))
# A = -4
# print(math.sqrt(A), type(math.sqrt(A))) # math domain error