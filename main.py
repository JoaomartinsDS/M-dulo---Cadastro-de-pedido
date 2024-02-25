from Classes import Pedido,Cliente
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = cpf in clientes
    return clientes_filtrados




def main():
    pedidos = {}
    clientes = {}
    while True:
        print(""" 
                1 - cadastrar cliente
                2 - criar pedido
                3 - sair

            """)
        opcao = int(input("Escolha a opção desejada: "))
        if opcao == 1:
            cpf = int(input("Digite seu cpf: "))
            cliente = filtrar_cliente(cpf,clientes)
            if cliente:
                print("Cliente ja cadastrado")
                continue
            nome = input("Digite seu nome: ")
            endereco = input("Digite seu endereço")
            data_nascimento = input("Digite sua data de nascimento:")
            cria_cliente = Cliente.criar_cliente(clientes,cpf,nome,data_nascimento,endereco)
        elif opcao == 2:
            cpf = int(input("Digite seu cpf: "))
            cliente = filtrar_cliente(cpf,clientes)
            if cliente:
                pedido = len(pedidos) + 1
                cadastra_pedido = Pedido()
                cadastra_pedido.realizar_pedido(cpf,pedido,pedidos)
            else: 
                print("Cliente não cadastrado, efetue o cadastro para realizar o pedido!")
        elif opcao == 3:
            print("Obrigado por testar nosso sistema!")
            return
            
        
main()