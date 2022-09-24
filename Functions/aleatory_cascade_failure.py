# estas funciones atacan a nodos y enlaces de forma aleatoria causando una falla en cascada
def aleatory_cascade_failure(G,Initial_Capacity,Resiliencia,Number_Attacks):
  """
  (Graph,float,float,int) -------> (G,Vector con los daños, vector con el número de ataques)
  Esta funcion luego de atacar un nodo aleatoriamente ejecuta el algoritmo de falla en cascada y te entrega como resultado
  el grafo atacado, un vector con los daños por ataque y un vector con el número de ataques
  """
  load1 = nx.load_centrality(G)
  keys1 = list(load1.keys())
  Capacity = []
  #se definen condiciones iniciales
  for i in range(len(keys1)): 
    q = (1+Initial_Capacity)*load1[keys1[i]]
    Capacity.append(q)
  DAMAGE = []
  ATTACK = []
  #en este for se ejecutan los ataques
  for i in range(Number_Attacks): 
    NodosBC = len(max(nx.connected_components(G), key = len))
    #registramos el daño con el cambio en el tamaño de la componente principal y los ataques
    DAMAGE.append(NodosBC/len(G.nodes()))
    ATTACK.append(i) 
    #se remueve un nodo aleatoriamente
    remove_aleatory(G,1) 
    DELETE_NODES = []
    load = nx.load_centrality(G)
    for j in G.nodes():
      #calculamos el valor de load sobre el cual el nodo colapsara con 100% de probabilidad
      val = Resiliencia*Capacity[keys1.index(j)] 
      if load[j] > val: 
        #enlistamos los nodos que colapsan con 100% de probabilidad
        DELETE_NODES.append(j) 
      else:
        #se decide si un nodo que ha superado su capacidad colapsa
        if load[j] > Capacity[keys1.index(j)]: 
          k = st.uniform.rvs()
          P = (1/(Resiliencia-1))*(load[j]/Capacity[keys1.index(j)] -1)
          if k <= P:
            ##enlistamos los nodos colapsados
            DELETE_NODES.append(j) 
    ##se eliminan los nodos colapsados
    G.remove_nodes_from(DELETE_NODES) 
  return G,ATTACK,DAMAGE

def edge_aleatory_cascade_failure(G,Initial_Capacity,Resiliencia,Number_attacks):
  """
  (Graph,float,float,int) -------> (G,Vector con los daños, vector con el numero de ataques)
  Esta funcion luego de atacar un enlace aleatoriamente ejecuta el algoritmo de falla en cascada y te entrega como resultado
  el grafo atacado, un vector con los daños por ataque y un vector con el número de ataques
  """
  load1 = nx.edge_load_centrality(G)
  keys1 = list(load1.keys())
  Capacity = []
  #se definen condiciones iniciales
  for i in range(len(keys1)): 
    q = (1+Initial_Capacity)*load1[keys1[i]]
    Capacity.append(q)
  DAMAGEEDGE = []
  ATTACK = []
  #en este for se ejecutan los ataques
  for i in range(Number_attacks): 
    NodosBC = len(max(nx.connected_components(G), key = len))
    #registramos el daño con el cambio en el tamaño de la componente principal y los ataques
    DAMAGEEDGE.append(NodosBC/len(G.nodes()))
    ATTACK.append(i) 
    #se remueve un edge aleatoriamente
    edge_remove_aleatory(G,1) 
    DELETE_EDGES = []
    load = nx.edge_load_centrality(G)
    for j in G.edges():
    #calcula el valor de load sobre el cual un nodo colapsara con 100% de probabilidad
      val = Resiliencia*Capacity[keys1.index(j)] 
      if load[j] > val: 
         #enlistamos nodos colapsados
        DELETE_EDGES.append(j) 
      else:
         #se elige si un nodo que ha superado su capacidad colapsa
        if load[j] > Capacity[keys1.index(j)]: 
          k = st.uniform.rvs()
          P = (1/(Resiliencia -1))*(load[j]/Capacity[keys1.index(j)] - 1)
          if k <= P:
            DELETE_EDGES.append(j)
    #enlistamos nodos colapsados
    G.remove_edges_from(DELETE_EDGES) 
  return G, ATTACK, DAMAGEEDGE


