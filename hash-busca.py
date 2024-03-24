from collections import defaultdict                 # Importa a função defaultdict do módulo collections
import random                                       # Importa o módulo random
import timeit                                       # Importa o módulo timeit
import concurrent.futures                           # Importa o módulo concurrent.futures para execução paralela de tarefas em threads separadas (ThreadPoolExecutor) 

class Pessoa:                                           # Define a classe Pessoa
    def __init__(self, cpf, nome, telefone, senha):     # Define o método construtor da classe Pessoa com os atributos cpf, nome, telefone e senha
        self.cpf = cpf                                  # Atributo cpf 
        self.nome = nome                                # Atributo nome 
        self.telefone = telefone                       # Atributo telefone
        self.senha = senha                             # Atributo senha


def gerar_dados_pessoa():                                              # Define a função gerar_dados_pessoa
    cpf = ''.join(random.choices('0123456789', k=11))                  # Gera um CPF aleatório com 11 dígitos numéricos  
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"       # Formata o CPF no padrão XXX.XXX.XXX-XX  
    nome = 'Pessoa' + str(random.randint(1, 1000))                     # Gera um nome aleatório para a pessoa 
    telefone = random.randint(100000000, 999999999)                    # Gera um número de telefone aleatório com 9 dígitos 
    senha = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))      # Gera uma senha aleatória com 8 caracteres 
    return Pessoa(cpf_formatado, nome, telefone, senha)                 # Retorna um objeto da classe Pessoa com os dados gerados

class Hashing:                                                        # Define a classe Hashing
    def __init__(self, tamanho):                                 # Define o método construtor da classe Hashing com o atributo tamanho 
        self.tabela = defaultdict(list)                         # Cria um dicionário com listas vazias para armazenar os registros 

    def inserir(self, pessoa):                                  # Define o método inserir da classe Hashing com o parâmetro pessoa 
        self.tabela[pessoa.cpf].append(pessoa)                  # Adiciona a pessoa na lista correspondente ao CPF na tabela hash 

    def buscar_por_cpf(self, cpf):                              # Define o método buscar_por_cpf da classe Hashing com o parâmetro cpf 
        return self.tabela.get(cpf, [])                         # Retorna a lista de pessoas correspondente ao CPF, ou uma lista vazia se não houver registros

class BuscaBinaria:                                             # Define a classe BuscaBinaria 
    def __init__(self, tamanho):                                # Define o método construtor da classe BuscaBinaria com o atributo tamanho 
        self.registros = [None] * tamanho                       # Cria uma lista de tamanho n com valores nulos 
        self.tamanho = 0                                        # Inicializa o tamanho da lista como 0 

    def inserir(self, pessoa):                                  # Define o método inserir da classe BuscaBinaria com o parâmetro pessoa 
        if self.tamanho == 0:                                   # Se a lista estiver vazia  
            self.registros[0] = pessoa                         # Insere a pessoa na primeira posição da lista 
            self.tamanho += 1                                   # Incrementa o tamanho da lista 
            return                                               
        inicio = 0                                              # Define o início da lista como 0 
        fim = self.tamanho - 1                                  # Define o fim da lista como o tamanho da lista - 1 
        while inicio <= fim:                                    # Enquanto o início for menor ou igual ao fim 
            meio = (inicio + fim) // 2                          # Calcula o meio da lista 
            if self.registros[meio].cpf == pessoa.cpf:                       # Se o CPF da pessoa for igual ao CPF do registro no meio da lista 
                return                                                  # CPF já existe, não é necessário inserir novamente  
            elif self.registros[meio].cpf < pessoa.cpf:               # Se o CPF da pessoa for maior que o CPF do registro no meio da lista 
                inicio = meio + 1                                     # Atualiza o início da lista para o meio + 1 
            else: 
                fim = meio - 1                                        # Atualiza o fim da lista para o meio - 1 
        posicao = inicio                                               # Define a posição de inserção como o início da lista 
        for i in range(self.tamanho, posicao, -1):                    # Para cada posição i no intervalo do tamanho da lista até a posição de inserção, decrementando de 1 em 1 
            self.registros[i] = self.registros[i - 1]               # Desloca os registros para a direita 
        self.registros[posicao] = pessoa                           # Insere a pessoa na posição de inserção 
        self.tamanho += 1                                         # Incrementa o tamanho da lista

    def buscar_por_cpf(self, cpf):                               # Define o método buscar_por_cpf da classe BuscaBinaria com o parâmetro cpf 
        inicio = 0                                               # Define o início da lista como 0
        fim = self.tamanho - 1                                   # Define o fim da lista como o tamanho da lista - 1 
        while inicio <= fim:                                     # Enquanto o início for menor ou igual ao fim
            meio = (inicio + fim) // 2                           # Calcula o meio da lista
            if self.registros[meio].cpf == cpf:                  # Se o CPF do registro no meio da lista for igual ao CPF de pesquisa
                return self.registros[meio]                      # Retorna o registro
            elif self.registros[meio].cpf < cpf:                 # Se o CPF do registro no meio da lista for menor que o CPF de pesquisa 
                inicio = meio + 1                                # Atualiza o início da lista para o meio + 1 
            else:
                fim = meio - 1                                   # Atualiza o fim da lista para o meio - 1 
        return None

class BuscaSequencial:                                                              # Define a classe BuscaSequencial 
    def __init__(self):                     
        self.registros = set()                                                   # Cria um conjunto vazio para armazenar os registros

    def inserir(self, pessoa):                                                  # Define o método inserir da classe BuscaSequencial com o parâmetro pessoa
        self.registros.add(pessoa.cpf)                                         # Adiciona o CPF da pessoa ao conjunto de registros
     
    def buscar_por_cpf(self, cpf):                                            # Define o método buscar_por_cpf da classe BuscaSequencial com o parâmetro cpf 
        if cpf in self.registros:                                               # Se o CPF estiver no conjunto de registros
            return cpf                                                        # Retorna o CPF   
        return None                                                       # Caso contrário, retorna None


def teste_insercao(estrutura, dados):                                    # Define a função teste_insercao com os parâmetros estrutura e dados 
    tempo_inicial = timeit.default_timer()                            # Marca o tempo inicial
    for dado in dados:                                             # Para cada dado no conjunto de dados
        estrutura.inserir(dado)                                # Insere o dado na estrutura
    tempo_final = timeit.default_timer()                        # Marca o tempo final
    tempo_total = tempo_final - tempo_inicial                  # Calcula o tempo total
    return tempo_total


def teste_pesquisa(estrutura, dados, quantidade_pesquisas):                # Define a função teste_pesquisa com os parâmetros estrutura, dados e quantidade_pesquisas
    tempos_pesquisa = [] 
    for _ in range(quantidade_pesquisas):   
        dado_pesquisa = random.choice(dados)                                # Seleciona um dado aleatório para pesquisa
        tempo_inicial = timeit.default_timer()                              # Marca o tempo inicial
        estrutura.buscar_por_cpf(dado_pesquisa.cpf)                          # Realiza a pesquisa
        tempo_final = timeit.default_timer()                                 # Marca o tempo final
        tempo_pesquisa = tempo_final - tempo_inicial                            # Calcula o tempo de pesquisa
        tempos_pesquisa.append(tempo_pesquisa)                                  # Adiciona o tempo de pesquisa à lista de tempos
    tempo_medio = sum(tempos_pesquisa) / len(tempos_pesquisa)                  # Calcula o tempo médio de pesquisa
    return tempo_medio


tamanho_conjunto = 100                                                           # Define o tamanho do conjunto de dados              


dados = [gerar_dados_pessoa() for _ in range(tamanho_conjunto)]                   # Gera um conjunto de dados com 100 registros de pessoas


with concurrent.futures.ThreadPoolExecutor() as executor:                                # Cria um ThreadPoolExecutor para execução paralela de tarefas em threads separadas
    hashing = Hashing(tamanho_conjunto)                                                  # Cria um objeto da classe Hashing
    tempo_insercao_hashing = executor.submit(teste_insercao, hashing, dados)                # Executa a função teste_insercao em uma thread separada
    tempo_pesquisa_hashing = executor.submit(teste_pesquisa, hashing, dados, 100)             # Executa a função teste_pesquisa em uma thread separada


with concurrent.futures.ThreadPoolExecutor() as executor:                                      # Cria um ThreadPoolExecutor para execução paralela de tarefas em threads separadas
    busca_binaria = BuscaBinaria(tamanho_conjunto)                                              # Cria um objeto da classe BuscaBinaria
    tempo_insercao_busca_binaria = executor.submit(teste_insercao, busca_binaria, dados)         # Executa a função teste_insercao em uma thread separada
    tempo_pesquisa_busca_binaria = executor.submit(teste_pesquisa, busca_binaria, dados, 100)   # Executa a função teste_pesquisa em uma thread separada


with concurrent.futures.ThreadPoolExecutor() as executor:                                           # Cria um ThreadPoolExecutor para execução paralela de tarefas em threads separadas
    busca_sequencial = BuscaSequencial()                                                             # Cria um objeto da classe BuscaSequencial
    tempo_insercao_busca_sequencial = executor.submit(teste_insercao, busca_sequencial, dados)         # Executa a função teste_insercao em uma thread separada
    tempo_pesquisa_busca_sequencial = executor.submit(teste_pesquisa, busca_sequencial, dados, 100)     # Executa a função teste_pesquisa em uma thread separada

    
print("Tempos de inserção:") 
print("Hashing:", tempo_insercao_hashing.result())
print("Busca Binária:", tempo_insercao_busca_binaria.result())
print("Busca Sequencial:", tempo_insercao_busca_sequencial.result())
print("\nTempos de pesquisa:")
print("Hashing:", tempo_pesquisa_hashing.result())
print("Busca Binária:", tempo_pesquisa_busca_binaria.result())
print("Busca Sequencial:", tempo_pesquisa_busca_sequencial.result())
