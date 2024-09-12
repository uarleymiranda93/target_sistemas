import random

def calc_faturamento():
    # Inicializa um vetor com 365 posições com valor 0
    vetor_faturamento = [0] * 365

    # Preenche o vetor com valores de faturamento aleatórios entre 1000 e 10000
    for i in range(365):
        # Decide aleatoriamente se o dia terá faturamento
        if random.choice([True, False]):
            # Se sim, define o faturamento para o dia
            vetor_faturamento[i] = random.randint(1000, 10000)

    # Filtra os dias com faturamento (ignora os dias sem faturamento)
    faturamentos_validos = []
    for valor in vetor_faturamento:
        if valor > 0:
            faturamentos_validos.append(valor)

    # Verifica se existem faturamentos válidos
    if not faturamentos_validos:
        print("Nenhum faturamento registrado.")
        return

    # Encontra o menor valor de faturamento
    menor_faturamento = min(faturamentos_validos)
    # Encontra o maior valor de faturamento
    maior_faturamento = max(faturamentos_validos)

    # Calcula a média anual
    soma_faturamentos = sum(faturamentos_validos)
    numero_dias_com_faturamento = len(faturamentos_validos)
    media_anual = soma_faturamentos / numero_dias_com_faturamento

    # Conta o número de dias com faturamento superior à média anual
    dias_acima_da_media = 0
    for valor in faturamentos_validos:
        if valor > media_anual:
            dias_acima_da_media += 1

    # Exibe os resultados
    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média anual: {dias_acima_da_media}")

# Chamada da função
calc_faturamento()