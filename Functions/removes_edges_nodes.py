#las siguientes 4 funciones remueven N nodos o enlaces de forma aleatoria y dirigida de un grafo dado como input

#remueve nodos con mayor load
def remove_hubs_load(G,nodos_removidos): 
  """
  (G, #nodos_removidos) ---------> G
  """
  for i in range(nodos_removidos):
    keys = list(nx.load_centrality(G).keys())
    values = list(nx.load_centrality(G).values())
    maxval = max(values)
    casilla_nodo = values.index(maxval)
    G.remove_node(keys[casilla_nodo])
  return G


#remueve edges con mayor load
def edge_remove_hub_load(G,edges_removidos): 
  """
  (G,#edges_removidos) -------> G
  """
  for i in range(edges_removidos):
    keys = list(nx.edge_load_centrality(G).keys())
    values = list(nx.load_centrality(G).values())
    maxval = max(values)
    casilla_edge = values.index(maxval)
    G.remove_edge(keys[casilla_edge][0],keys[casilla_edge][1])
  return G

#remueve nodos aleatoriamente
def remove_aleatory(G,nodos_removidos): 
  """
  (G,#nodos_removidos) -----------> G
  """
  keys = list(G.nodes())
  for i in range(nodos_removidos):
    remove_node = np.random.randint(0,G.number_of_nodes())
    remnode = keys[remove_node]
    if (remnode in G) == True:
      G.remove_node(remnode)
  return G

#remueve edges aleatoriamente
def edge_remove_aleatory(G,edges_removidos): 
  """
  (G,#edges_removidos) ------> G
  """
  for i in range(edges_removidos):
    remove_edge = np.random.randint(0,len(nx.edges(G)))
    if (remove_edge in G) ==True:
      G.remove_edge(list(nx.edges(G))[remove_edge][0],list(nx.edges(G))[remove_edge][1])
  return G

