import csv

total = 0

with open ("vendas.txt","w") as f:
     f.write("100\n200\n150\n300")

with open("vendas.txt","r") as f:
    for linha in f:
        valor = int(linha)
        total += valor
    
    print("Total de vendas:", total)