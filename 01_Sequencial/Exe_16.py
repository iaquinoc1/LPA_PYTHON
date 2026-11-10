tamanho = int(input("Informe o tamanho do arqiovo em MB: "))
velocidade = int(input("Informe a velocidade da conexão em mbps: "))

tempo = (tamanho * 8) / velocidade / 60

print (f'Tempo aproximado de download: {tempo: .2f} minutos')