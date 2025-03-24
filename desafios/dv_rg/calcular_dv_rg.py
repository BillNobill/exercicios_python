def calcular_dv_rg(rg):
    # Verificação de erro
    if len(rg) != 8 or not rg.isdigit():
        raise ValueError("O RG deve ter exatamente 8 dígitos numéricos.")

    # Pesos de 2 a 7 (repetindo, se necessário)
    pesos = [2, 3, 4, 5, 6, 7]

    # Multiplicação dos dígitos pelos pesos (da direita para esquerda)
    soma = 0
    for i in range(8):
        peso = pesos[i % len(pesos)]
        soma += int(rg[7 - i]) * peso

    # Cálculo do dígito verificador
    resto = soma % 11
    if resto == 0 or resto == 1:
        dv = 0
    else:
        dv = 11 - resto
    return dv