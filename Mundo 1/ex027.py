"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
nome = input("Nome: ")
nome = nome.title().split()
print("Primeiro: {}".format(nome[0]))
print("Último: {}".format(nome[-1]))
