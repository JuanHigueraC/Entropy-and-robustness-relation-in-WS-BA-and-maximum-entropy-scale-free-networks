#Este algoritmo muestrea secuencias de grado con la distribucion del vector de probabilidades acumuladas, entrega como output secuencia de grado promedio
def Deg_Sec_Prom(Muestreo_seq,Number_nodes,Probability_distribution,kmin):
  """
  (num_muestras,number_nodes,probability_distribution,kimn) ----------------> (degree_sequence_prom)
  esta funcion hace uso de Degree_Sec_Generator
  """
  #matriz donde se guardaran las distintas secuencias a muestrear
  degree_sequences = [] 
  #por cada i generamos una secuencia
  for i in range(Muestreo_seq): 
    degree_sequences.append([]) 
    for k in range(10000):
      #generamos y validamos la secuencia
      Degree_Sequence = Degree_Sec_Generator(Probability_distribution,Number_nodes,kmin) 
      if nx.is_valid_degree_sequence_havel_hakimi(Degree_Sequence) == True:
        if nx.is_connected(nx.havel_hakimi_graph(Degree_Sequence)) == True: 
          #la ordenamos, esto con el fin de darle una identidad a los nodos acorde a su puesto en el ranking de medida
          Degree_Sequence.sort() 
          #este for es para agregar la secuencia de grado a la matriz creada inicialmente
          for l in range(len(Degree_Sequence)):
            degree_sequences[i].append(Degree_Sequence[l])
          break
  Degree_sequence_prom = [] #esta parte del codigo calcular el promedio
  for i in range(Number_nodes):
    sum = 0
    for j in range(Muestreo_seq):
      sum = sum + degree_sequences[j][i]
    Degree_sequence_prom.append(sum/Muestreo_seq)
  return Degree_sequence_prom
