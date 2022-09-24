#esta funcion recibe vector de probabilidades acumulada y un entero, te entrega un grafo generado con el algoritmo expuesto en el proyecto que sustenta este respositorio
def maxent_generator(cum_probability,number_nodes,kmin):
  """
  (cum_probability,number_nodes,kmin) -----> G
  esta funcion recibe vector de probabilidades acumulada, un numero de nodos y un grado minimo. 
  te entrega un grafo generado con el algoritmo expuesto de maxima entropia expuesto en el proyecto
  """
  for k in range(1000000000000):
          #generamos la secuencia y validamos que permita generar un grafo simple conectado
          Degree_Sequence = Degree_Sec_Generator(cum_probability,number_nodes,kmin) 
          if nx.is_valid_degree_sequence_havel_hakimi(Degree_Sequence) == True:
            if nx.is_connected(nx.havel_hakimi_graph(Degree_Sequence)) == True: 
             #la ordenamos, esto con el fin de darle una identidad a los nodos acorde a su puesto en el ranking de medida
              Degree_Sequence.sort()
              #creamos el grafo con el algoritmo havel hakimi
              Grafo = nx.havel_hakimi_graph(Degree_Sequence) 
              break
  #muestreamos los grafos con una secuencia de grado dada a partir de edge switching
  nx.double_edge_swap(Grafo,nswap=1000,max_tries=150000)
  return Grafo
