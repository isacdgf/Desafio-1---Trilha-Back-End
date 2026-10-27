SistemaAtivo = True

totalBruto = 0
totalDeDesconto = 0
totalFinal = 0

ListaDeCompras = []
ListadeIdade = []

while SistemaAtivo:
    while True:
        valorDaCompra = float(input("Digite o valor da compra:"))
        if(valorDaCompra < 0):
            print("Digite um valor valido!!")
        else:
            break;
    if(valorDaCompra != 0):
        while True:
            idade = int(input("Digite sua idade:"))
            if(idade <= 0):
                print("Digite um valor valido!!")
            else:
                break;

        valorFinalDaCompra = valorDaCompra
        
        if idade >= 65:
            valorFinalDaCompra = valorDaCompra * 0.8

        if valorFinalDaCompra > 100:
            valorFinalDaCompra = valorFinalDaCompra * 0.9



        descontoDaCompra = valorDaCompra - valorFinalDaCompra

        print(f"Valor total: R${valorFinalDaCompra}")

        totalFinal += valorFinalDaCompra
        totalDeDesconto += descontoDaCompra
       

        ListaDeCompras.append(valorFinalDaCompra)
        ListadeIdade.append(idade)
        print("------------------------------------------------")
    else:
        SistemaAtivo = False


        codigo = 1
        for i in range(len(ListaDeCompras)):
            
            print(f"Codigo de compra:{codigo} | Idade:{ListadeIdade[i]} | Valor:R${ListaDeCompras[i]:.2f}")
            codigo += 1 

        print(f"Total de compras:{codigo }")
        print(f"Total bruto{totalBruto}")
        print(f"Valor de descontos concedidos{totalDeDesconto}")
        print("------------------------------------------------------")
        print(f"Valor final com desconto:{totalFinal}")

        
        

        




        

