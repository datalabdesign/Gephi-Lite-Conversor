<img src="logo_lab_orange.png" alt="lab_logo" width="200"/>


# Conversor de Arquivos de Rede para Gephi Lite
Este repositório contém um Jupyter Notebook para converter arquivos de rede no formato GDF para formatos compatíveis com o Gephi Lite, como GraphML e GEXF. Criado pelo Professor Elias Bitencourt como material da disciplina de Métodos Digitais do curso de Design da Universidade do Estado da Bahia (UNEB), o objetivo desse notebook é facilitar o uso do Gephi Lite em atividades pedagógicas de análise de redes. A conversão automática de arquivos GDF permite que professores e estudantes integrem o Gephi Lite a ferramentas que geram esse formato, como o YouTube Data Tools e outras, mesmo em contextos com infraestrutura computacional mais limitada.

## Contexto

O Gephi Lite é uma versão simplificada do Gephi que roda diretamente no navegador, sem necessidade de instalação, o que o torna adequado para contextos pedagógicos com infraestrutura computacional limitada. Ele aceita arquivos nos formatos GraphML e GEXF, mas não é compatível com o formato GDF. Ferramentas como o YouTube Data Tools (YDT), por outro lado, geram arquivos em formato GDF, o que impede seu uso direto no Gephi Lite. Essa incompatibilidade exige que professores convertam os arquivos manualmente ou utilizem versões completas do Gephi, que demandam mais recursos. Este notebook automatiza a conversão de arquivos GDF para formatos compatíveis com o Gephi Lite, permitindo o uso conjunto do YDT e Gephi Lite em atividades didáticas de forma simplificada.

## Recursos

- **Conversão Automática**: Suporte para formatos GDF, GraphML e GEXF.
- **Compatibilidade com Gephi Lite**: Permite que arquivos de rede incompatíveis sejam adaptados para visualização no Gephi Lite.
- **Simplicidade**: Processo simplificado para realizar o upload, conversão e download de arquivos sem a necessidade de intervençoes adicionais.

## Uso

1. **Fazer o upload do arquivo GDF**:
   - Execute o notebook
   - Quando solicitado, faça o upload do arquivo de rede (.gdf).

2. **Conversão Automática**:
   - O código analisa o arquivo, ajusta os dados de nós e arestas, e converte para o formato especificado (GraphML ou GEXF).

3. **Download do Arquivo Convertido**:
   - Ao final do processo, o arquivo convertido estará disponível para download no Google Colab ou no diretório local.

## Requisitos

- **Python 3.6+**
- **Bibliotecas**: `pandas`, `networkx`
- **Ambiente**: Google Colab (para a versão notebook) 

## Sobre o Autor

Elias Bitencourt é Professor Adjunto no Curso de Design da Universidade do Estado da Bahia (UNEB). Tem Doutorado em Comunicação pela FACOM/UFBA e um Mestrado em Cultura e Sociedade pelo IHAC/UFBA. Foi pesquisador visitante no Centro Milieux no Canadá (2019). Atualmente, coordena o Datalab/Design (CNPq) na UNEB, que é um centro de pesquisa e desenvolvimento em visualização de dados e metodologias digitais. Sua pesquisa foca em visualização de dados, estudos de plataformas, imaginários digitais e os reflexos da mediação algorítmica nas relações sociais. É pesquisador colaborador no Inova Media Lab (Universidade Nova de Lisboa) e da rede internacional de pesquisa Public Data Lab.
