nome = input("Seja bem-vindo usuário, digite seu nome: ")
valor01 = input("Vamos fazer um programa que mostre o maior valor ou se eles são iguais.\n Digite o primeiro valor: ")
valor02 = input("Digite o segundo valor: ")
if valor01 > valor02:
    print(f"{nome}, o maior valor é {valor01}")
elif valor01 == valor02:
    print(f"{nome}, os dois valores {valor02} e {valor01} são iguais.")
else:
    print(f"{nome}, o maior valor é {valor02}")