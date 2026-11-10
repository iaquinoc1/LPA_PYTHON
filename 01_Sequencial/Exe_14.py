valor = float(input("Informe o valor do seu salário-hora: "))
ch = int(input("Informe a carga horária trabalhada: "))

bruto = valor * ch
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print ("Salário bruto = R$ ", bruto)
print ("Desconto de Imposto de Renda = R$", ir)
print ("Desconto de Previdência = R$ ", inss)
print ("Desconto do Sindicato = R$ ", sindicato)
print ("O salário líquido será de R$", liquido)