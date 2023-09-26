from random import shuffle
alu1 = str(input('Primeiro aluno: '))
alu2 = str(input('Segundo aluno: '))
alu3 = str(input('Terceiro aluno: '))
alu4 = str(input('Quarto aluno: '))
lista = [alu1, alu2, alu3, alu4]
shuffle(lista)
print(f'A ordem de apresentação será\n{lista}')