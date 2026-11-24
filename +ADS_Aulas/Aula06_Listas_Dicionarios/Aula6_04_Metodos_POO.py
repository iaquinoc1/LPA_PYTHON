#Uma lista é um objeto de uma classe dentro do Python
#Paradigmas de programação orientada a objetos (POO)

#A programação estruturada organiza o código em funções e
#procedimentos que operam sobre dados (muitas vezes separados),
#enquanto a programação orientada a objetos (POO) agrupa
#dados (atributos) e comportamentos (métodos) dentro de objetos,
#modelando entidades que interagem entre si

#Em Python, usar Programação Orientada a Objetos (POO)
#para manipular listas consiste em encapsular a lista
#como um atributo dentro de uma classe e criar métodos
#para gerenciar e proteger esses dados.

#Método é equivalente a função
#Modo de construir: variavel.funcao(parametro)
#Outro modo de ler: objeto.metodo(parametro)


#Gerenciador de Tarefas
#Neste exemplo, a classe ListaDeTarefas protege a lista 
#para que itens só sejam adicionados ou concluídos 
#por meio dos métodos definidos.

class ListaDeTarefas:
    def __init__(self):
        # A lista fica encapsulada dentro do objeto
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def concluir_primeira(self):
        if self.tarefas:
            return self.tarefas.pop(0)
        return "Nenhuma tarefa pendente."

    def mostrar(self):
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"{i}. {tarefa}")

# Uso:
minhas_tarefas = ListaDeTarefas()
minhas_tarefas.adicionar("Estudar POO")
minhas_tarefas.adicionar("Fazer exercícios")
minhas_tarefas.mostrar()

print("Concluída:", minhas_tarefas.concluir_primeira())


print(' ')

#Carrinho de Compras (Manipulando listas de objetos)
#Um dos usos mais comuns da POO é criar uma lista que 
#armazena instâncias de outra classe, facilitando cálculos e filtros.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []  # Vai guardar objetos do tipo Produto

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def listar_nomes(self):
        return [item.nome for item in self.itens]

# Uso:
carrinho = Carrinho()
carrinho.adicionar_produto(Produto("Teclado", 150.00))
carrinho.adicionar_produto(Produto("Mouse", 80.00))

print("Itens:", carrinho.listar_nomes())
print(f"Total: R$ {carrinho.calcular_total():.2f}")

print (" ")

#Lista com Validação e Métodos Especiais
#Pode-se adicionar regras de negócio antes de inserir 
#dados na lista e usar métodos especiais do Python 
#(como __len__ e __str__) para que o objeto 
#se comporte de forma mais natural.

class Turma:
    def __init__(self, limite_alunos):
        self.limite = limite_alunos
        self.alunos = []

    def matricular(self, nome):
        if len(self.alunos) >= self.limite:
            print(f"Não foi possível matricular {nome}: turma cheia!")
        elif nome in self.alunos:
            print(f"{nome} já está matriculado.")
        else:
            self.alunos.append(nome)

    def __len__(self):
        # Permite usar len(turma)
        return len(self.alunos)

    def __str__(self):
        # Permite usar print(turma)
        return f"Alunos ({len(self)}/{self.limite}): {', '.join(self.alunos)}"

# Uso:
turma_python = Turma(limite_alunos=2)
turma_python.matricular("Ana")
turma_python.matricular("Bruno")
turma_python.matricular("Carlos")  # Será bloqueado pela regra

print(turma_python)
