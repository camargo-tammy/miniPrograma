
while True:
   
    print("\nMenu:")
    print("1 - Calcular idade")
    print("2 - Calcular preço da compra")
    print("3 - Sair")

   
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    
    if opcao == "1":
        
        ano_nascimento = input("Digite o seu ano de nascimento: ")
   
        if ano_nascimento.isdigit():
            ano_nascimento = int(ano_nascimento)
            ano_atual = 2025  
            idade = ano_atual - ano_nascimento
            print(f"Sua idade é: {idade} anos.")
        else:
            print("Por favor, digite um ano válido.")

  
    elif opcao == "2":
        preco_total = 0  
        while True:
           
            preco = input("Digite o preço do item (ou 0 para finalizar): ")
            
            if preco.isdigit():
                preco = float(preco)
                if preco == 0:  
                    break
                preco_total += preco  
            else:
                print("Por favor, digite um valor numérico válido.")
       
        print(f"O total da sua compra é: R${preco_total:.2f}")

    elif opcao == "3":
        print("Saindo... Até logo!")
        break  

    else:
        print("Opção inválida! Tente novamente.")
