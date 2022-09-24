# Esta funcion calcula la entropia de distintas distribuciones de medidas para un grafo
def graph_entropys(G,nbins):
  """
  Recibe un grafo y entrega números
  (Graph) -----> Degree_Entropy, Eigenvector_Entropy, Betweenness_Entropy, Closeness_Entropy
  """
  EIGENVECTOR = []
  DEGREE = []
  BETWEENNESS = []
  CLOSENESS = []
  load = []
  #las siguientes 4 lineas producen 4 diccionarios con los nodos y sus centralidades correspondientes
  eigenvector = np.array(list(nx.eigenvector_centrality(G).values()))
  degree = np.array(list(nx.degree_centrality(G).values()))
  betweenness = np.array(list(nx.betweenness_centrality(G).values()))
  closeness = np.array(list(nx.closeness_centrality(G).values()))

  # aca se usa la funcion entropy_dist para calcular la entropia de las medidas
  closeness_Entropy = entropy_dist(closeness,nbins)
  degree_Entropy = entropy_dist(degree,nbins)
  eigenvector_Entropy = entropy_dist(eigenvector,nbins)
  betweenness_Entropy = entropy_dist(betweenness,nbins)
  return degree_Entropy, eigenvector_Entropy, betweenness_Entropy, closeness_Entropy
