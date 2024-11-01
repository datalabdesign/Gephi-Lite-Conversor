<img src="logo_lab_orange.png" alt="lab_logo" width="200"/>

# Conversor de Arquivos de Rede para Gephi Lite

Este repositório contém um Jupyter Notebook desenvolvido para converter arquivos de rede no formato GDF para formatos compatíveis com o Gephi Lite, como GraphML e GEXF. Criado pelo Professor Elias Bitencourt como parte do material didático da disciplina de Métodos Digitais do curso de Design da Universidade do Estado da Bahia (UNEB), o notebook facilita o uso do Gephi Lite em atividades pedagógicas de análise de redes. A ferramenta oferece conversão automática de arquivos GDF, além de um sistema de diagnóstico e geração de tabelas que auxilia no uso prático e exploratório de redes em contextos didáticos e de pesquisa.

## Contexto

O Gephi Lite é uma versão simplificada do Gephi que roda diretamente no navegador, sem necessidade de instalação, ideal para contextos pedagógicos com recursos computacionais limitados. Ele aceita arquivos nos formatos GraphML e GEXF, mas não é compatível com o formato GDF, o que limita o uso direto de ferramentas como o YouTube Data Tools (YDT) no Gephi Lite. Essa incompatibilidade exigia que professores convertessem arquivos manualmente ou utilizassem a versão completa do Gephi, que pode não ser possível em razão de limitações técnicas dos equipamentos acessíveis aos estudantes. Este notebook automatiza essa conversão, simplificando o uso conjunto do YDT e Gephi Lite em atividades didáticas e minimizando as barreiras tecnológicas para o ensino de análise de redes em cenários tecnologicamente mais restritivos.

Como recurso adicional, o notebook também gera um relatório detalhado da rede e exporta tabelas de nós e arestas em formato CSV. Essas funcionalidades fornecem uma visão abrangente da rede, incluindo quantidade de nós e arestas, tipo de rede (dirigida ou não dirigida), atributos de nós e arestas, e verificações de consistência. Esse diagnóstico prévio permite a estudantes e pesquisadores validar a estrutura da rede e identificar inconsistências (como nós isolados ou arestas duplicadas) antes da visualização, facilitando o entendimento da rede em seus aspectos estruturais e variáveis.

A exportação das tabelas de nós e arestas facilita uso didático e exploratório do conversor. Para o ensino, as tabelas ajudam a ilustrar como um grafo é construído “nos bastidores” e oferecem uma base para atividades de importação e construção de redes no Gephi a partir das tabelas, sendo útil para alunos que estão aprendendo os conceitos de análise de redes.

A possibilidade de exportar tabelas de redes processadas no Gephi Lite adiciona uma funcionalidade que ele não possui nativamente, diferentemente do Gephi completo, que permite a exportação direta de tabelas de nós e arestas. Com essa funcionalidade, é possível exportar dados enriquecidos após a análise no Gephi Lite, como comunidades (clusters), cores e graus, e realizar análises adicionais. Isso faz do Conversor um recurso complementar para pesquisadores, professores e estudantes que necessitam acessar as tabelas para análises detalhadas, mas que possuem acesso apenas ao Gephi Lite.

___

## Recursos

- **Conversão Automática**: Suporte para arquivos em formato GDF, convertendo-os para GraphML ou GEXF, facilitando a integração com o Gephi Lite e outras ferramentas que requerem compatibilidade nesses formatos.

- **Relatório de Rede**: Gera um relatório detalhado com informações estruturadas sobre a rede, incluindo:
  - **Quantidade de Nós e Arestas**: Número total de nós e arestas no grafo, proporcionando uma visão geral do tamanho e complexidade da rede.
  - **Tipo de Rede**: Identifica se a rede é dirigida ou não dirigida.
  - **Exemplos de Nós e Arestas**: Fornece exemplos aleatórios de nós e arestas, ajudando a contextualizar a estrutura da rede e validar a conversão.
  - **Atributos Associados aos Nós e Arestas**: Lista os atributos disponíveis para os nós e as arestas, facilitando a compreensão das variáveis presentes para cada nó e aresta, o que auxilia no planejamento de análises e na exploração didática da rede.

- **Verificações de Inconsistências**: Realiza uma série de checagens automáticas para detectar potenciais erros ou anomalias na rede, incluindo:
   - **Nós Isolados**: Identifica nós que não possuem conexões, o que pode indicar inconsistências ou dados que precisam de revisão.
   - **Arestas Duplicadas**: Verifica a presença de arestas repetidas (exceto em redes multigrafo), facilitando a remoção de redundâncias.
   - **Inconsistências de Direção**: Para redes dirigidas, verifica se há arestas contraditórias, ajudando a garantir uma direção consistente entre os nós conectados.
   - **Atributos Incompletos nas Arestas**: Confere se há arestas com atributos faltantes, possibilitando uma revisão mais criteriosa.
   - **Validação de Tipos de Dados**: Detecta automaticamente os tipos de atributos nos nós e arestas e verifica se os valores estão no formato esperado (e.g., valores numéricos como contagem de visualizações), mantendo a integridade dos dados para análise posterior.

- **Exportação de Tabelas de Nós e Arestas**: Cria arquivos CSV de nós e arestas, o que permite que estudantes e pesquisadores:
  - Visualizem, editem e manipulem os dados em planilhas ou outras ferramentas de análise.
  - Recriem e estudem a construção de redes em plataformas como o Gephi Lite, que não permite exportar essas tabelas diretamente, ou realizem análises adicionais.
  - Façam uso didático das tabelas para entender a estrutura e variáveis do grafo, ou ainda construam redes a partir de tabelas externas, facilitando o ensino da modelagem de redes.

- **Compatibilidade com Gephi Lite**: Garante que arquivos incompatíveis sejam adaptados para visualização e análise no Gephi Lite, promovendo a flexibilidade do uso em contextos de aprendizado ou pesquisa com infraestrutura limitada.

- **Interface Simples**: Uma interface de carregamento, conversão e download de arquivos fácil de usar, que não exige configurações adicionais, oferecendo acessibilidade tanto para iniciantes quanto para usuários avançados. 

## Uso

1. **Acione o script**:
   - Execute o notebook no Google Colab clicando no botão de execução.

2. **Escolha do Formato de Saída**:
   - No menu drop-down, selecione `GraphML` ou `GEXF` como formato de saída:
     - **GEXF**: Recomendado para redes dinâmicas ou temporais e uso no Gephi completo.
     - **GraphML**: Ideal para redes com atributos complexos e análise exploratória no Gephi Lite.

3. **Upload do Arquivo GDF**:
   - Pressione o botão `Selecionar Arquivo`
   - Quando aparecer o botão `Escolher Arquivo`, selecione o arquivo de rede no formato .gdf que deseja converter.

4. **Conversão Automática e Geração de Relatório**:
   - O código processa o arquivo de rede, ajusta dados de nós e arestas e converte para o formato especificado.
   - Um relatório detalhado é gerado automaticamente, exibindo informações essenciais e identificando possíveis inconsistências na rede, como nós isolados, direção da rede e atributos ausentes.

5. **Download do Arquivo Convertido, Relatório e Tabelas**:
   - O notebook oferece download dos arquivos convertidos (GraphML ou GEXF), do relatório de diagnóstico e das tabelas de nós e arestas (em formato CSV), que podem ser usados para análise em planilhas ou softwares de rede.

## Exemplo de Relatório Gerado

O relatório gerado pelo notebook inclui um diagnóstico inicial da rede, ajudando estudantes e pesquisadores a entenderem a estrutura da rede, validarem a conversão e corrigirem possíveis erros. Exemplo:

```
Relatório da Rede - Gephi Lite Conversor

Quantidade de Nós: 120
Quantidade de Arestas: 180
Tipo da Rede: Não dirigida
Formato de Saída: GRAPHML

Exemplo de Nó: Node_001
Exemplo de Aresta: Node_001 - Node_002

Atributos dos Nós: name, label, category, created_at
Atributos das Arestas: weight, directed

Inconsistências Encontradas:
- Nós isolados: 3
- Arestas duplicadas: 5
- Inconsistências de direção: 0
- Atributos incompletos nas arestas:
    - atributo 'directed': 2 arestas com valor ausente
    - atributo 'weight': 3 arestas com valor ausente

Como citar:
Bitencourt, E. (2024). *Gephi Lite Conversor* (Versão 1.0) [Software].
Datalab Design, Universidade do Estado da Bahia - UNEB, Salvador, Brasil.
https://github.com/datalabdesign/Gephi-Lite-Conversor
```

## Exemplo das Tabelas de Nós e Arestas

O notebook também exporta tabelas de nós e arestas, permitindo a análise e edição dos dados em outras ferramentas. Exemplos de saída em CSV:

### Tabela de Nós (nodes.csv)

| Node ID    | name      | label        | category | created_at |
|------------|-----------|--------------|----------|------------|
| Node_001   | Alice     | Student      | Class A  | 2024-10-31 |
| Node_002   | Bob       | Researcher   | Class B  | 2024-10-29 |
| Node_003   | Carol     | Instructor   | Class A  | 2024-10-27 |

### Tabela de Arestas (edges.csv)

| Source     | Target     | weight | directed |
|------------|------------|--------|----------|
| Node_001   | Node_002   | 1.5    | False    |
| Node_002   | Node_003   | 2.0    | True     |
| Node_001   | Node_003   | 1.0    | False    |

As tabelas de nós e arestas fornecem uma visão detalhada dos dados de rede, facilitando a análise e permitindo que professores e estudantes manipulem informações de rede de forma independente em outras plataformas de análise.

## Requisitos

- **Python 3.6+**
- **Bibliotecas**: `pandas`, `networkx`
- **Ambiente**: Google Colab (para a versão notebook)

## Benefícios para Estudantes e Pesquisadores

Para professores e estudantes em disciplinas de análise de redes, o relatório permite diagnosticar e verificar a rede antes da visualização, facilitando a compreensão das variáveis e dos atributos associados a cada nó e aresta. A identificação de inconsistências, como nós isolados ou arestas duplicadas, ajuda a assegurar que a rede esteja corretamente configurada para análise. A exportação de tabelas em CSV amplia a flexibilidade para que estudantes e pesquisadores explorem os dados de rede de forma independente, permitindo manipulações em planilhas e outras ferramentas, facilitando o estudo das características estruturais da rede e das variáveis atribuídas.

## Sobre o Autor

Elias Bitencourt é Professor Adjunto no Curso de Design da Universidade do Estado da Bahia (UNEB), com Doutorado em Comunicação pela FACOM/UFBA e Mestrado em Cultura e Sociedade pelo IHAC/UFBA. Foi pesquisador visitante no Centro Milieux, Canadá, em 2019. Atualmente, coordena o Datalab/Design (CNPq) na UNEB, um centro de pesquisa em visualização de dados e metodologias digitais. Sua pesquisa foca em visualização de dados, estudos de plataformas, imaginários digitais e mediação algorítmica nas relações sociais. Ele é pesquisador colaborador no Inova Media Lab (Universidade Nova de Lisboa) e na rede internacional Public Data Lab.
