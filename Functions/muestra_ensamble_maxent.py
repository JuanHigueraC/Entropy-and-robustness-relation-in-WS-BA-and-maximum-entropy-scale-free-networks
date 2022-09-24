#este algoritmo muestrea el ensamble de redes por medio del algoritmo de maxima entropia y te entrega su matriz de adyacencia promedio
def muestra_ensamble_maxent(muestra,number_of_nodes,P,kmin):
  """
  (num_muestra, num_nodes,cum_probab_distribut) -------> (Degree_sequence_prom,adjacencia_insilico)
  """
  connectivity_matrix = np.zeros((muestra, number_of_nodes, number_of_nodes))
  #por cada l se genera un grafo
  for l in range(muestra):
      #generamos un grafo usando el algoritmo de maxima entropia
      G = maxent_generator(P,number_of_nodes,kmin) 
      adjacency = nx.adjacency_matrix(G)
      for i in range(number_of_nodes):
        for j in range(number_of_nodes):
         #guardamos las matrices de adyacencias de los grafos muestreados
          connectivity_matrix[l][i][j] = adjacency[(i,j)] 
          
  #ahora promediamos las matrices de adyacencia muestreadas muestreadas
  adjacencia_insilico = np.zeros((number_of_nodes,number_of_nodes)) 
  for i in range(number_of_nodes):
    for j in range(number_of_nodes):
      adjprom = 0
      for l in range(muestra):
        adjprom = adjprom + connectivity_matrix[l][i][j]
      adjprom = adjprom/muestra 
      adjacencia_insilico[i][j] = adjprom 
  return adjacencia_insilico
