for indice, item in enumerate(["a", "b", "c"], start=1):
    print(indice, item)

valores = [10, 20, 30]

for valor in valores:
    print(valor * 2)

chaves = ["host", "porta"]
valores = ["localhost", 5432]
for k, v in zip(chaves, valores):
    print(f"{k}={v}")
