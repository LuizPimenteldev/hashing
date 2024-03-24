from collections import defaultdict
import random
import timeit
import concurrent.futures

class Pessoa:
    def __init__(self, cpf, nome, telefone, senha):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.senha = senha

# Função para gerar dados de pessoa aleatórios
def gerar_dados_pessoa():
    cpf = ''.join(random.choices('0123456789', k=11))
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    nome = 'Pessoa' + str(random.randint(1, 1000))
    telefone = random.randint(100000000, 999999999)
    senha = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
    return Pessoa(cpf_formatado, nome, telefone, senha)

class Hashing:
    def __init__(self, tamanho):
        self.tabela = defaultdict(list)

    def inserir(self, pessoa):
        self.tabela[pessoa.cpf].append(pessoa)

    def buscar_por_cpf(self, cpf):
        return self.tabela.get(cpf, [])

class BuscaBinaria:
    def __init__(self, tamanho):
        self.registros = [None] * tamanho
        self.tamanho = 0

    def inserir(self, pessoa):
        if self.tamanho == 0:
            self.registros[0] = pessoa
            self.tamanho += 1
            return
        inicio = 0
        fim = self.tamanho - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.registros[meio].cpf == pessoa.cpf:
                return  # CPF já existe, não é necessário inserir novamente
            elif self.registros[meio].cpf < pessoa.cpf:
                inicio = meio + 1
            else:
                fim = meio - 1
        posicao = inicio
        for i in range(self.tamanho, posicao, -1):
            self.registros[i] = self.registros[i - 1]
        self.registros[posicao] = pessoa
        self.tamanho += 1

    def buscar_por_cpf(self, cpf):
        inicio = 0
        fim = self.tamanho - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.registros[meio].cpf == cpf:
                return self.registros[meio]
            elif self.registros[meio].cpf < cpf:
                inicio = meio + 1
            else:
                fim = meio - 1
        return None

class BuscaSequencial:
    def __init__(self):
        self.registros = set()  # Usar um conjunto para armazenar apenas os CPFs

    def inserir(self, pessoa):
        self.registros.add(pessoa.cpf)

    def buscar_por_cpf(self, cpf):
        if cpf in self.registros:
            return cpf
        return None

# Função para inserir registros em uma estrutura de dados e medir o tempo de inserção
def teste_insercao(estrutura, dados):
    tempo_inicial = timeit.default_timer()
    for dado in dados:
        estrutura.inserir(dado)
    tempo_final = timeit.default_timer()
    tempo_total = tempo_final - tempo_inicial
    return tempo_total

# Função para realizar pesquisas em uma estrutura de dados e medir o tempo médio de pesquisa
def teste_pesquisa(estrutura, dados, quantidade_pesquisas):
    tempos_pesquisa = []
    for _ in range(quantidade_pesquisas):
        dado_pesquisa = random.choice(dados)  # Escolhe aleatoriamente um dado para pesquisa
        tempo_inicial = timeit.default_timer()
        estrutura.buscar_por_cpf(dado_pesquisa.cpf)
        tempo_final = timeit.default_timer()
        tempo_pesquisa = tempo_final - tempo_inicial
        tempos_pesquisa.append(tempo_pesquisa)
    tempo_medio = sum(tempos_pesquisa) / len(tempos_pesquisa)
    return tempo_medio

# Definição do tamanho do conjunto de dados de exemplo
tamanho_conjunto = 100  # Por exemplo, 10.000 registros

# Gerar dados de exemplo
dados = [gerar_dados_pessoa() for _ in range(tamanho_conjunto)]

# Teste de inserção e pesquisa para Hashing em paralelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    hashing = Hashing(tamanho_conjunto)
    tempo_insercao_hashing = executor.submit(teste_insercao, hashing, dados)
    tempo_pesquisa_hashing = executor.submit(teste_pesquisa, hashing, dados, 100)

# Teste de inserção e pesquisa para BuscaBinaria em paralelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    busca_binaria = BuscaBinaria(tamanho_conjunto)
    tempo_insercao_busca_binaria = executor.submit(teste_insercao, busca_binaria, dados)
    tempo_pesquisa_busca_binaria = executor.submit(teste_pesquisa, busca_binaria, dados, 100)

# Teste de inserção e pesquisa para BuscaSequencial em paralelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    busca_sequencial = BuscaSequencial()
    tempo_insercao_busca_sequencial = executor.submit(teste_insercao, busca_sequencial, dados)
    tempo_pesquisa_busca_sequencial = executor.submit(teste_pesquisa, busca_sequencial, dados, 100)

# Imprimindo os resultados
print("Tempos de inserção:")
print("Hashing:", tempo_insercao_hashing.result())
print("Busca Binária:", tempo_insercao_busca_binaria.result())
print("Busca Sequencial:", tempo_insercao_busca_sequencial.result())
print("\nTempos de pesquisa:")
print("Hashing:", tempo_pesquisa_hashing.result())
print("Busca Binária:", tempo_pesquisa_busca_binaria.result())
print("Busca Sequencial:", tempo_pesquisa_busca_sequencial.result())
