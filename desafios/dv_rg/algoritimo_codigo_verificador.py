import re
import calcular_dv_rg

rg = input("Digite os 8 primeiros dígitos do RG: ")
rg_limpo = re.sub(r'[.\-\s]', '', rg)

try:
    dv = calcular_dv_rg(rg_limpo)
    print(f"O dígito verificador do RG {rg} é: {dv}")
except ValueError as e:
    print(f"Erro: {e}")
