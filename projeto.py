# Define um CPF para validação (sem os dígitos verificadores)
cpf = '89828065045'

# Pega os primeiros 9 dígitos do CPF
nove_digitos = cpf[:9]

# Cálculo do primeiro dígito verificador
contador_regressivo_1 = 10  # Contador começa em 10 para o primeiro dígito

resultado_digito_1 = 0
for digito in nove_digitos:
    # Multiplica cada dígito pelo contador regressivo e soma os resultados
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1  # Decrementa o contador

# Calcula o primeiro dígito verificador
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0  # Se o resto for > 9, dígito é 0

# Adiciona o primeiro dígito verificador aos 9 dígitos originais
dez_digitos = nove_digitos + str(digito_1)

# Cálculo do segundo dígito verificador
contador_regressivo_2 = 11  # Contador começa em 11 para o segundo dígito

resultado_digito_2 = 0
for digito in dez_digitos:
    # Multiplica cada dígito pelo contador regressivo e soma os resultados
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1  # Decrementa o contador

# Calcula o segundo dígito verificador (CORREÇÃO: havia um erro de sintaxe aqui)
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0  # Se o resto for > 9, dígito é 0

# Verifica se os dígitos calculados correspondem aos dígitos do CPF original
cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado:
    print(f'O CPF {cpf} é válido!')
else:
    print(f'O CPF {cpf} é inválido!')