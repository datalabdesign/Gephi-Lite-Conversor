<img src="logo_lab_orange.png" alt="lab_logo" width="200"/>


# Conversor de Arquivos de Rede para Gephi Lite
Este repositório contém um código em Python, desenvolvido como recurso didático para converter arquivos de rede no formato GDF para formatos compatíveis com o Gephi Lite, como GraphML e GEXF. Criado pelo Professor Elias Bitencourt como parte do material da disciplina de Métodos Digitais do curso de Design da Universidade do Estado da Bahia (UNEB), o objetivo é simplificar a análise de redes usando o YouTube Data Tools e o Gephi Lite para estudantes e professores em sala de aula.

## Contexto

Ferramentas como o YouTube Data Tools nem sempre produzem arquivos diretamente compatíveis com o Gephi Lite, o que pode dificultar o uso combinado das duas ferramentas em cenários que os estudantes não têm infraestrutura disponível para usar a versão completa do Gephi. Este notebook e o script em Python automatizam a conversão dos arquivos, facilitando o uso do Yutube Data Tools e do Gephi Lite em atividades pedagógicas.

## Recursos

- **Conversão Automática**: Suporte para formatos GDF, GraphML e GEXF.
- **Compatibilidade com Gephi Lite**: Permite que arquivos de rede incompatíveis sejam adaptados para visualização no Gephi Lite.
- **Simplicidade**: Processo simplificado para realizar o upload, conversão e download de arquivos sem procedimentos manuais.

## Uso

1. **Fazer o upload do arquivo GDF**:
   - Execute o notebook ou o script em Python.
   - Quando solicitado, faça o upload do arquivo de rede (.gdf).

2. **Conversão Automática**:
   - O código analisa o arquivo, ajusta os dados de nós e arestas, e converte para o formato especificado (GraphML ou GEXF).

3. **Download do Arquivo Convertido**:
   - Ao final do processo, o arquivo convertido estará disponível para download no Google Colab ou no diretório local.

## Requisitos

- **Python 3.6+**
- **Bibliotecas**: `pandas`, `networkx`
- **Ambiente**: Google Colab (para a versão notebook) ou Python local

## Exemplo de Execução

```python
# Chamando a função para iniciar a conversão
upload_and_convert(output_format='graphml')  # Altere para 'gexf' para outro formato de saída
```

## Sobre o Autor

Elias Bitencourt é Professor Adjunto no Curso de Design da Universidade do Estado da Bahia (UNEB). Tem Doutorado em Comunicação pela FACOM/UFBA e um Mestrado em Cultura e Sociedade pelo IHAC/UFBA. Foi pesquisador visitante no Centro Milieux no Canadá (2019). Atualmente, coordena o Datalab/Design (CNPq) na UNEB, que é um centro de pesquisa e desenvolvimento em visualização de dados e metodologias digitais. Sua pesquisa foca em visualização de dados, estudos de plataformas, imaginários digitais e os reflexos da mediação algorítmica nas relações sociais. É pesquisador colaborador no Inova Media Lab (Universidade Nova de Lisboa) e da rede internacional de pesquisa Public Data Lab.
