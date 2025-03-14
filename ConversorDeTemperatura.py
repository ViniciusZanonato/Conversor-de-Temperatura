#  origem
temp_ori = int(input('Escolha a unidade de temperatura que deseja ser convertida:\n1) Celsius\n2) Fahrenheit\n3) Kelvin\nDigite o número da opção: '))

#  destino
temp_desti = int(input('Escolha para qual unidade de temperatura será convertida:\n1) Celsius\n2) Fahrenheit\n3) Kelvin\nDigite o número da opção: '))

# opções válidas
if (temp_ori == 1 or temp_ori == 2 or temp_ori == 3) and (temp_desti == 1 or temp_desti == 2 or temp_desti == 3):
    #valor da temperatura
    valor = float(input("Digite o valor da temperatura: "))

    # Conversão
    if temp_ori == 1:  # Celsius
        if temp_desti == 1:  
            resultado = valor
            unidade_destino = "Celsius"
        elif temp_desti == 2:  
            resultado = (valor * 9/5) + 32  # Fórmula Fahrenheit
            unidade_destino = "Fahrenheit"
        elif temp_desti == 3:  
            resultado = valor + 273.15
            unidade_destino = "Kelvin"

    elif temp_ori == 2:  # Fahrenheit
        if temp_desti == 1:  
            resultado = (valor - 32) * 5/9  # Fórmula Celsius
            unidade_destino = "Celsius"
        elif temp_desti == 2:  
            resultado = valor
            unidade_destino = "Fahrenheit"
        elif temp_desti == 3:  
            resultado = (valor - 32) * 5/9 + 273.15  # Fórmula Kelvin
            unidade_destino = "Kelvin"

    elif temp_ori == 3:  # Kelvin
        if destino == 1:  
            resultado = valor - 273.15
            unidade_destino = "Celsius"
        elif temp_desti == 2:  
            resultado = (valor - 273.15) * 9/5 + 32  # Fórmula Fahrenheit
            unidade_destino = "Fahrenheit"
        elif temp_desti == 3: 
            resultado = valor
            unidade_destino = "Kelvin"

    # resultado
    print(f"{valor} na unidade escolhida é igual a {round(resultado, 2)} {unidade_destino}")
else:
    print("Opção inválida! Selecione uma opção válida entre 1, 2 ou 3 para a unidade de origem e destino.")
