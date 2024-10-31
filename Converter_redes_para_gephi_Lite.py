# In[4]:
import pandas as pd
import networkx as nx
from google.colab import files
import os

def load_graph_from_file(file_path):
    """
    Carrega um arquivo de grafo e detecta o formato automaticamente (GDF, GEXF, ou GraphML).

    :param file_path: Caminho para o arquivo do grafo.
    :return: Um objeto Graph do NetworkX.
    """
    extension = os.path.splitext(file_path)[-1].lower()

    if extension == '.gdf':
        return load_gdf(file_path)
    elif extension == '.gexf':
        return nx.read_gexf(file_path)
    elif extension == '.graphml':
        return nx.read_graphml(file_path)
    else:
        raise ValueError("Formato de arquivo não suportado. Use GDF, GEXF ou GraphML.")

def load_gdf(gdf_file_path):
    """
    Converte um arquivo GDF em um objeto Graph do NetworkX.

    :param gdf_file_path: Caminho para o arquivo GDF.
    :return: Um objeto Graph do NetworkX.
    """
    with open(gdf_file_path, 'r') as file:
        lines = file.readlines()

    # Identificar linhas de definição de nós e arestas
    node_def_line_candidates = [i for i, line in enumerate(lines) if 'nodedef>' in line]
    if not node_def_line_candidates:
        raise ValueError("A seção de nós (nodedef) não foi encontrada no arquivo GDF.")
    node_def_line = node_def_line_candidates[0]
    nodes_start = node_def_line + 1

    edges_start = None
    for i, line in enumerate(lines):
        if 'edgedef>' in line:
            edges_start = i + 1
            break
    if edges_start is None:
        raise ValueError("A seção de arestas (edgedef) não foi encontrada no arquivo GDF.")

    # Carregar dados de nós e arestas
    node_columns = lines[node_def_line].strip().replace('nodedef>', '').split(',')
    nodes_data = [line.strip().split(',') for line in lines[nodes_start:edges_start - 1]]
    nodes_df = pd.DataFrame(nodes_data, columns=node_columns)

    edge_columns = lines[edges_start - 1].strip().replace('edgedef>', '').split(',')
    edges_data = [line.strip().split(',') for line in lines[edges_start:]]
    edges_df = pd.DataFrame(edges_data, columns=edge_columns)

    # Criar grafo e adicionar nós e arestas
    G = nx.Graph()
    node_id_column = node_columns[0]
    for _, row in nodes_df.iterrows():
        G.add_node(row[node_id_column], **row.to_dict())

    source_column = edge_columns[0]
    target_column = edge_columns[1]
    for _, row in edges_df.iterrows():
        G.add_edge(row[source_column], row[target_column], **{col: row[col] for col in edge_columns if col not in [source_column, target_column]})

    return G

def convert_graph_to_format(G, original_file_path, output_format='graphml'):
    """
    Converte um grafo NetworkX para o formato especificado.

    :param G: Objeto Graph do NetworkX.
    :param original_file_path: Caminho do arquivo original.
    :param output_format: Formato de saída desejado ('graphml' ou 'gexf').
    :return: Caminho para o arquivo convertido.
    """
    output_file = original_file_path.replace(os.path.splitext(original_file_path)[-1], f'.{output_format}')

    if output_format == 'graphml':
        nx.write_graphml(G, output_file)
    elif output_format == 'gexf':
        nx.write_gexf(G, output_file)
    else:
        raise ValueError("Formato de saída inválido. Escolha 'graphml' ou 'gexf'.")

    print(f"Arquivo convertido para {output_format} e salvo em: {output_file}")
    return output_file

def upload_and_convert(output_format='graphml'):
    """
    Realiza o upload de um arquivo de grafo e converte-o para o formato especificado.

    :param output_format: Formato de saída, pode ser 'graphml' ou 'gexf'.
    """
    uploaded = files.upload()  # Upload do arquivo de grafo
    for filename in uploaded.keys():
        G = load_graph_from_file(filename)
        converted_file = convert_graph_to_format(G, filename, output_format=output_format)
        files.download(converted_file)  # Baixar o arquivo convertido

#Chamando a função
upload_and_convert(output_format='graphml')  # Altere para 'gexf' se preferir GEXF


