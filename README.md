# hashing e busca binária

INTEGRANTES:

LUIZ EDUARDO 

RICARDO JOSÉ 

PAULO JUNIO

CONSIDERAÇÕES:

Tamanho do Conjunto de Dados:
Para conjuntos de dados pequenos, a diferença de desempenho entre as estruturas de dados pode não ser tão significativa. No entanto, para conjuntos de dados maiores, a eficiência das operações de inserção e pesquisa se torna crucial.

Frequência de Inserções e Pesquisas:
Se o aplicativo envolver principalmente inserções e pesquisas ocasionais em um grande conjunto de dados, a estrutura de hashing pode ser uma escolha eficiente devido à sua complexidade média de tempo O(1) para operações de inserção e pesquisa.
Se o aplicativo envolver muitas pesquisas e poucas inserções ou vice-versa, a escolha entre busca sequencial e busca binária pode depender da ordenação dos dados e das características específicas das operações.

Ordenação dos Dados:
A busca binária requer que os dados estejam ordenados, enquanto a busca sequencial e o hashing não têm essa exigência. Portanto, se os dados já estiverem ordenados ou se a ordenação for aceitável, a busca binária pode ser uma opção eficiente.
Se a ordenação dos dados for impraticável ou não desejada, a busca sequencial ou o hashing podem ser mais adequados.

Colisões de Hash:
Ao usar hashing, é importante considerar a possibilidade de colisões, onde duas chaves diferentes resultam no mesmo índice de hash. O tratamento de colisões, como encadeamento ou resolução de colisões por sondagem, pode afetar o desempenho geral da estrutura de hashing.

Eficiência de Memória:
Embora o código atual não analise especificamente a eficiência de memória das estruturas de dados, é importante considerar a quantidade de memória utilizada por cada estrutura, especialmente para conjuntos de dados grandes.





Referências:
gerador de CPF
https://gist.github.com/lucascnr/24c70409908a31ad253f97f9dd4c6b7c


Hashing Algorithms and Security - Computerphile
https://www.youtube.com/watch?v=b4b8ktEV4Bg&pp=ygUHaGFzaGluZw%3D%3D 

Hashing in Python: Using Hashlib Library for Secure Hashing
https://www.youtube.com/watch?v=i-h0CtKde6w

