def exibir_maior_valor(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else:
        return valor2

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

maior_valor = exibir_maior_valor(valor1, valor2)
print("O maior valor recebido é:", maior_valor)
