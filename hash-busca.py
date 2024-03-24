from collections import defaultdict                     # Importa a classe defaultdict do módulo collections para criar um dicionário com valores padrão para a tabela hash 
import random                                                                # Importa o módulo random para gerar números aleatórios para os dados de teste  
import timeit                                                                # Importa o módulo timeit para medir o tempo de execução dos testes de inserção e pesquisa 

class Pessoa:                                                              # Define a classe Pessoa para representar os dados de uma pessoa 
    def __init__(self, cpf, nome, telefone, senha):                      # Define o método construtor da classe Pessoa com os atributos cpf, nome, telefone e senha
        self.cpf = cpf 
        self.nome = nome
        self.telefone = telefone
        self.senha = senha

def gerar_dados_pessoa():                                                            # Define a função gerar_dados_pessoa para gerar dados de teste para a classe Pessoa 
    cpf = ''.join(random.choices('0123456789', k=11))                                   # Gera um CPF aleatório com 11 dígitos numéricos  
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"                  # Formata o CPF gerado no formato XXX.XXX.XXX-XX 
    nome = f'Pessoa{random.randint(1, 1000)}'                                       # Gera um nome aleatório para a pessoa 
    telefone = random.randint(100000000, 999999999)                                   # Gera um número de telefone aleatório com 9 dígitos numéricos 
    senha = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8)) # Gera uma senha aleatória com 8 caracteres alfanuméricos 
    return Pessoa(cpf_formatado, nome, telefone, senha)                          # Retorna um objeto da classe Pessoa com os dados gerados 

class Hashing:                                                             # Define a classe Hashing para implementar a tabela hash 
    def __init__(self, tamanho):                                     # Define o método construtor da classe Hashing com o tamanho da tabela hash 
        self.tabela = defaultdict(list)                            # Inicializa a tabela hash como um dicionário com listas como valores padrão 

    def inserir(self, pessoa):                                     # Define o método inserir para adicionar uma pessoa na tabela hash 
        self.tabela[pessoa.cpf].append(pessoa)                 # Adiciona a pessoa na lista correspondente ao CPF na tabela hash 

    def buscar_por_cpf(self, cpf):                               # Define o método buscar_por_cpf para buscar uma pessoa na tabela hash pelo CPF 
        return self.tabela.get(cpf, [])                         # Retorna a lista de pessoas correspondente ao CPF na tabela hash ou uma lista vazia se o CPF não existir 

class BuscaBinaria:                                                   # Define a classe BuscaBinaria para implementar a busca binária 
    def __init__(self, tamanho):                               # Define o método construtor da classe BuscaBinaria com o tamanho do vetor de registros 
        self.registros = [None] * tamanho                   # Inicializa o vetor de registros com o tamanho especificado 
        self.tamanho = 0                                           # Inicializa o tamanho do vetor de registros como zero 

    def inserir(self, pessoa):                                  # Define o método inserir para adicionar uma pessoa no vetor de registros 
        if self.tamanho == 0:                                     # Verifica se o vetor de registros está vazio 
            self.registros[0] = pessoa                             # Adiciona a pessoa na primeira posição do vetor de registros 
            self.tamanho += 1                                     # Incrementa o tamanho do vetor de registros 
            return
        inicio, fim = 0, self.tamanho - 1                            # Define os índices de início e fim para a busca binária 
        while inicio <= fim:                                           # Realiza a busca binária para encontrar a posição de inserção da pessoa 
            meio = (inicio + fim) // 2                                # Calcula o índice do meio do vetor de registros 
            if self.registros[meio].cpf == pessoa.cpf:              # Verifica se o CPF da pessoa é igual ao CPF do registro do meio
                return                                             # Retorna se o CPF da pessoa já existe no vetor de registros 
            elif self.registros[meio].cpf < pessoa.cpf:            # Verifica se o CPF da pessoa é maior que o CPF do registro do meio 
                inicio = meio + 1                                  # Atualiza o índice de início para a metade superior do vetor de registros 
            else:
                fim = meio - 1                                       # Atualiza o índice de fim para a metade inferior do vetor de registros 
        posicao = inicio                                             # Define a posição de inserção da pessoa no vetor de registros 
        self.registros[posicao + 1:] = self.registros[posicao:-1]     # Desloca os registros para a direita a partir da posição de inserção 
        self.registros[posicao] = pessoa                            # Adiciona a pessoa na posição de inserção 
        self.tamanho += 1                                          # Incrementa o tamanho do vetor de registros 

    def buscar_por_cpf(self, cpf):                               # Define o método buscar_por_cpf para buscar uma pessoa no vetor de registros pelo CPF 
        inicio, fim = 0, self.tamanho - 1                           # Define os índices de início e fim para a busca binária 
        while inicio <= fim:                                         # Realiza a busca binária para encontrar a pessoa com o CPF especificado 
            meio = (inicio + fim) // 2                             # Calcula o índice do meio do vetor de registros 
            if self.registros[meio].cpf == cpf:                  # Verifica se o CPF da pessoa do meio é igual ao CPF especificado 
                return self.registros[meio]                     # Retorna a pessoa do meio se o CPF for igual ao CPF especificado 
            elif self.registros[meio].cpf < cpf:                # Verifica se o CPF da pessoa do meio é menor que o CPF especificado 
                inicio = meio + 1                               # Atualiza o índice de início para a metade superior do vetor de registros 
            else:
                fim = meio - 1                                  # Atualiza o índice de fim para a metade inferior do vetor de registros 
        return None

class BuscaSequencial:                                             # Define a classe BuscaSequencial para implementar a busca sequencial 
    def __init__(self):                                        # Define o método construtor da classe BuscaSequencial 
        self.registros = set()                              # Inicializa o conjunto de registros como um conjunto vazio 

    def inserir(self, pessoa):                              # Define o método inserir para adicionar uma pessoa no conjunto de registros 
        self.registros.add(pessoa.cpf)                   # Adiciona o CPF da pessoa no conjunto de registros 

    def buscar_por_cpf(self, cpf):                         # Define o método buscar_por_cpf para buscar uma pessoa no conjunto de registros pelo CPF 
        return cpf if cpf in self.registros else None      # Retorna o CPF se o CPF existir no conjunto de registros ou None caso contrário 

def teste_insercao(estrutura, dados):                                 # Define a função teste_insercao para testar o tempo de inserção dos dados na estrutura de dados 
    tempo_inicial = timeit.default_timer()                            # Marca o tempo inicial antes da inserção dos dados 
    for dado in dados:                                               # Insere cada dado na estrutura de dados 
        estrutura.inserir(dado)                                       # Insere o dado na estrutura de dados 
    tempo_final = timeit.default_timer()                              # Marca o tempo final após a inserção dos dados
    return tempo_final - tempo_inicial                              # Retorna o tempo total de inserção dos dados na estrutura de dados 

def teste_pesquisa(estrutura, dados, quantidade_pesquisas):           # Define a função teste_pesquisa para testar o tempo de pesquisa dos dados na estrutura de dados 
    tempos_pesquisa = []                                              # Inicializa uma lista para armazenar os tempos de pesquisa dos dados 
    for _ in range(quantidade_pesquisas):                           # Realiza a quantidade especificada de pesquisas de dados na estrutura de dados 
        dado_pesquisa = random.choice(dados).cpf                    # Seleciona um dado aleatório para pesquisa na estrutura de dados 
        tempo_inicial = timeit.default_timer()                       # Marca o tempo inicial antes da pesquisa do dado 
        estrutura.buscar_por_cpf(dado_pesquisa)                      # Pesquisa o dado na estrutura de dados 
        tempo_final = timeit.default_timer()                        # Marca o tempo final após a pesquisa do dado 
        tempos_pesquisa.append(tempo_final - tempo_inicial)        # Adiciona o tempo de pesquisa do dado na lista de tempos de pesquisa 
    return sum(tempos_pesquisa) / len(tempos_pesquisa)           # Retorna a média dos tempos de pesquisa dos dados na estrutura de dados 

tamanhos_conjunto = [10000, 100000, 1000000]                                          # Define os tamanhos dos conjuntos de dados para os testes 

for tamanho_conjunto in tamanhos_conjunto:                                            # Realiza os testes para cada tamanho de conjunto de dados
    print(f"\nResultados para conjunto de dados com {tamanho_conjunto} elementos:")      # Exibe o tamanho do conjunto de dados atual 
    dados = [gerar_dados_pessoa() for _ in range(tamanho_conjunto)]                    # Gera os dados de teste para o tamanho do conjunto de dados atual

    hashing = Hashing(tamanho_conjunto)                                                  # Cria uma tabela hash com o tamanho do conjunto de dados atual 
    tempo_insercao_hashing = teste_insercao(hashing, dados)                              # Testa o tempo de inserção dos dados na tabela hash
    tempo_pesquisa_hashing = teste_pesquisa(hashing, dados, 100)                         # Testa o tempo de pesquisa dos dados na tabela hash 

    busca_binaria = BuscaBinaria(tamanho_conjunto)                                           # Cria um vetor de registros com o tamanho do conjunto de dados atual 
    tempo_insercao_busca_binaria = teste_insercao(busca_binaria, dados)                       # Testa o tempo de inserção dos dados no vetor de registros
    tempo_pesquisa_busca_binaria = teste_pesquisa(busca_binaria, dados, 100)                 # Testa o tempo de pesquisa dos dados no vetor de registros

    busca_sequencial = BuscaSequencial()                                                    # Cria um conjunto de registros vazio 
    tempo_insercao_busca_sequencial = teste_insercao(busca_sequencial, dados)               # Testa o tempo de inserção dos dados no conjunto de registros 
    tempo_pesquisa_busca_sequencial = teste_pesquisa(busca_sequencial, dados, 100)          # Testa o tempo de pesquisa dos dados no conjunto de registros 

    print("Tempos de inserção:")
    print("Hashing:", tempo_insercao_hashing)
    print("Busca Binária:", tempo_insercao_busca_binaria)
    print("Busca Sequencial:", tempo_insercao_busca_sequencial)
    print("\nTempos de pesquisa:")
    print("Hashing:", tempo_pesquisa_hashing)
    print("Busca Binária:", tempo_pesquisa_busca_binaria)
    print("Busca Sequencial:", tempo_pesquisa_busca_sequencial)

    
