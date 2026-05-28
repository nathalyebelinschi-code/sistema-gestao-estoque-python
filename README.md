# 📦 Sistema de Gestão de Estoque em Python (v1.0)

Este projeto simula um sistema básico de gerenciamento e controle de estoque baseado em console, desenvolvido como parte da **Experiência Prática 2** da Universidade Positivo, para a disciplina de Programação de Computadores para a empresa fictícia *DataCode Solutions*. 

O objetivo principal da aplicação é manipular dados estruturados em memória, oferecendo um menu interativo contínuo para visualização, entrada e saída de produtos, além de tratar com segurança regras de negócio críticas.

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3.14
- **Estruturas de Dados:** Dicionários aninhados (*Dicionário de Dicionários*) para busca e atualização eficiente em tempo constante $O(1)$.
- **Estruturas de Repetição:** Laço contínuo `while True` com condição de parada explícita (`break`).
- **Controle de Fluxo e Condicionais:** Estruturas `if-elif-else` aninhadas para camadas múltiplas de segurança.
- **Tratamento de Strings:** Métodos nativos `.strip()` e `.capitalize()` para higienização e padronização das entradas do usuário.
- **Formatação de Dados:** Uso de *f-strings* com especificadores de precisão de casas decimais (`:.2f`) para valores monetários.
- **Guia de Estilo:** Código totalmente padronizado seguindo as diretrizes da **PEP 8** (convenção *snake_case* e indentações de 4 espaços).

## 🚀 Funcionalidades Mapeadas

1. **Visualizar Estoque Atual:** Exibe de forma limpa a listagem de todos os produtos, suas respectivas quantidades e preços unitários.
2. **Registrar Entrada de Produto (Reposição):** Permite adicionar novas unidades ao estoque de um item existente após validar a sua presença no sistema.
3. **Registrar Saída de Produto (Venda):** Processa saídas deduzindo a quantidade vendida do saldo em memória e calcula o valor financeiro total da transação.
4. **Mecanismos de Segurança (Fallbacks):**
   - Valida se o produto solicitado existe no sistema para evitar falhas de interrupção (*KeyError*).
   - Bloqueia operações de venda caso a quantidade solicitada seja maior que o saldo disponível, emitindo alerta de **"Estoque insuficiente"**.
   - Captura e trata opções inválidas digitadas no menu principal.
   - Encerramento controlado e gracioso da aplicação.

## 📷 Demonstração de Execução

Aqui está o funcionamento das principais rotinas rodando diretamente no terminal do VS Code:

### 🔹 Menu Principal e Listagem (Opção 1)
<img width="1604" height="1031" alt="print1" src="https://github.com/user-attachments/assets/9de7c033-a422-4332-92b5-7a078373219a" />


### 🔹 Entrada e Reposição de Itens (Opção 2)
<img width="1736" height="1023" alt="print2" src="https://github.com/user-attachments/assets/64b2406e-4c2b-4523-b8cc-4a4e3757500d" />


### 🔹 Venda Segura com Validação de Saldo (Opção 3)
<img width="1919" height="1010" alt="print3" src="https://github.com/user-attachments/assets/01434389-0656-4738-a83a-b33bda1e7811" />

