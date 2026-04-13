"""
Pesquisa de Opinião sobre Atendimento
"""

# Inicializando os acumuladores

excelente_total = 0
ruim_total = 0
bom_total = 0

# Uso do FOR coletar dados dos entrevistados
for i in range(50):
    print(f"Entrevistado {i + 1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    opiniao_valida = False
    opiniao = int(input("Opinião sobre o atendimento (1: EXCELENTE, 2: BOM, 3: RUIM): "))
    
    # Verificando a opinião do entrevistado
    while not opiniao_valida:
        match opiniao:
            case 1:
                excelente_total += 1
                opiniao_valida = True
                print("registrado EXCELENTE")
            case 2:
                bom_total += 1
                opiniao_valida = True
                print("registrado BOM")
            case 3:
                ruim_total += 1
                opiniao_valida = True
                print("registrado RUIM")
            case _:
                print("Opinião inválida. Por favor, digite 1, 2 ou 3.")
                opiniao = int(input("Opinião sobre o atendimento (1: EXCELENTE, 2: BOM, 3: RUIM): "))

# Placar Final
print("\nResultados da pesquisa:")
print("--------------------------------------")
print(f"Quantidade de respostas 'EXCELENTE': {excelente_total}")
print(f"Quantidade de respostas 'BOM': {bom_total}")
print(f"Quantidade de respostas 'RUIM': {ruim_total}")
print(f"Total de entrevistados: {excelente_total + bom_total + ruim_total}")
print("--------------------------------------")