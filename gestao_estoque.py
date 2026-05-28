# ==============================================================================
# Script: gestao_estoque.py
# Propósito: Simular um sistema básico de gerenciamento e controle de estoque
# Contexto: Experiência Prática 2 - DataCode Solutions
# ==============================================================================

# --- ETAPA 1: Inicialização da Estrutura de Dados ---
# Dicionário estruturado onde a chave primária é o nome do produto
estoque = {
    "Notebook": {"quantidade": 10, "preco": 3500.00},
    "Mouse": {"quantidade": 50, "preco": 80.00},
    "Teclado": {"quantidade": 30, "preco": 150.00}
}

# --- ETAPA 2: Laço de Repetição do Menu Interativo ---
while True:
    print("\n" + "="*35)
    print("      DATACODE SOLUTIONS - ESTOQUE      ")
    print("="*35)
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    print("="*35)
    
    # Coleta da opção tratando espaços vazios adicionais
    opcao = input("Escolha uma opção (1-4): ").strip()
    
    # --- ETAPA 3: Controle de Fluxo Condicional ---
    
    # OPÇÃO 1: Visualização do Estoque Atual
    if opcao == "1":
        print("\n--- ESTOQUE ATUAL ---")
        for produto, info in estoque.items():
            print(f"Produto: {produto} | Quantidade: {info['quantidade']} | Preço: R$ {info['preco']:.2f}")
            
    # OPÇÃO 2: Entrada de Produto (Reposição)
    elif opcao == "2":
        print("\n--- REGISTRAR ENTRADA DE PRODUTO ---")
        nome_produto = input("Digite o nome do produto para reposição: ").strip().capitalize()
        
        # Validação de existência do produto no dicionário
        if nome_produto in estoque:
            quantidade_entrada = int(input(f"Digite a quantidade a ser adicionada para {nome_produto}: "))
            if quantidade_entrada > 0:
                estoque[nome_produto]["quantidade"] += quantidade_entrada
                print(f"Sucesso: {quantidade_entrada} unidades adicionadas ao estoque.")
            else:
                print("Erro: A quantidade deve ser maior que zero.")
        else:
            print("Produto não encontrado.")
            
    # OPÇÃO 3: Saída de Produto (Venda) com Múltiplas Validações
    elif opcao == "3":
        print("\n--- REGISTRAR SAÍDA DE PRODUTO ---")
        nome_produto = input("Digite o nome do produto para saída: ").strip().capitalize()
        
        # 1ª Camada de Segurança: Validação de existência da chave
        if nome_produto in estoque:
            quantidade_solicitada = int(input(f"Digite a quantidade a ser retirada de {nome_produto}: "))
            
            if quantidade_solicitada <= 0:
                print("Erro: A quantidade de saída deve ser maior que zero.")
            # 2ª Camada de Segurança: Verificação de saldo disponível
            elif quantidade_solicitada > estoque[nome_produto]["quantidade"]:
                print("Estoque insuficiente")
            else:
                estoque[nome_produto]["quantidade"] -= quantidade_solicitada
                valor_total = quantidade_solicitada * estoque[nome_produto]["preco"]
                print(f"Sucesso: {quantidade_solicitada} unidades retiradas de {nome_produto}.")
                print(f"Total da Venda: R$ {valor_total:.2f}")
        else:
            print("Produto não encontrado")
            
    # OPÇÃO 4: Encerramento Seguro do Sistema
    elif opcao == "4":
        print("\n" + "="*35)
        print("Encerrando o Sistema de Gestão de Estoque v1.0.")
        print("A DataCode Solutions agradece o seu contato. Até logo!")
        print("="*35)
        break
        
    # Fallback para entradas incorretas
    else:
        print("\n⚠ Erro Operacional: Opção inválida!")
        print("Por favor, selecione um comando válido de 1 a 4.")
