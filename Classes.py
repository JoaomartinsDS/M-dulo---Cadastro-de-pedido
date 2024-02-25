from datetime import datetime

class PessoaFisica:
    def __init__(self, nome, endereco, data_nascimento,cpf):
        self._nome = nome
        self._endereco = endereco
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    @property
    def endereco(self):
        return self._endereco
    @property
    def data_nascimento(self):
        return self._data_nascimento
    @property
    def cpf(self):
        return self._cpf
    
class Cliente(PessoaFisica):
    def __init__(self, nome, endereco, data_nascimento, cpf):
        super().__init__(nome, endereco, data_nascimento, cpf)
    
    
    def criar_cliente(clientes,cpf,nome,data_nascimento,endereco):
        clientes[cpf] = {nome:nome,data_nascimento:data_nascimento,endereco:endereco}
        print("Cliente cadastrado com sucesso!")
        def __str__(self) :
            return f"{self.__class__.__name__}: {[f"{chave}={valor}" for chave ,valor in self.__dict__.items()]}"
    
class Pedido:
    @property
    def cpf(self):
        return self._cpf
    @property
    def numero_do_pedido(self):
        return self._numero_do_pedido
    @property
    def data_do_pedido(self):
        return self._data_do_pedido
    
    def realizar_pedido(self,cpf,numero_do_pedido,pedidos):
        self._data_do_pedido = datetime.now()
        self._cpf = cpf
        self._numero_do_pedido = numero_do_pedido
        pedidos[cpf] = {self._numero_do_pedido,self._data_do_pedido}
        print("Pedido cadastrado com sucesso!")
