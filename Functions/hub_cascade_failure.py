#estas funciones atacan nodos y enlaces en base al ranking en la medida fload y causan una falla en cascada
# la falla en cascada se realiza recalculando el load en la red y eliminando con cierta probabilidad los nodos que tengan un load mayor 
# a su load_inicial*resiliencia, si el load supera un valor dado la probabilidad de eliminacion es 100%

def hub_cascade_failure(G,Initial_Capacity,Resiliencia,Number_Attacks):
  """
  (Graph,float,float,int) -------> (G)
  Esta funcion ataca nodos acorde a su ranking en la medida load y luego aplica una falla en cascada
  acorde a que nodos soportan un mayor load que el dado por su capacidad inicial y resiliencia
  """
  load1 = nx.load_centrality(G)
  keys1 = list(load1.keys())
  nodes = len(G.nodes())
  Capacity = []
  #se definen condiciones iniciales
  for i in range(len(keys1)): 
    q = (1+Initial_Capacity)*load1[keys1[i]]
    Capacity.append(q)
  DAMAGE = []
  ATTACK = []
  #en este for se ejecutan los ataques
  for i in range(Number_Attacks): 
    NodosBC = len(max(nx.connected_components(G), key=len))
    #registramos el daño con el cambio en el tamaño de la componente principal y los ataques
    DAMAGE.append(NodosBC/nodes) 
    ATTACK.append(i) 
    #se remueve el nodo con mayor load
    remove_hubs_load(G,1) 
    DELETE_NODES = []
    load = nx.load_centrality(G)
    for j in G.nodes():
      #calculamos el valor de load sobre el cual un nodo colapsara con 100% de seguridad
      val = Resiliencia*Capacity[keys1.index(j)] 
      if load[j] > val: 
        ##enlistamos los nodos que colapsaran con 100% de probabilidad
        DELETE_NODES.append(j) 
      else:
        #se elige si un nodo que ha superado su capacidad colapsa
        if load[j] > Capacity[keys1.index(j)]:
          k = st.uniform.rvs()
          P = (1/(Resiliencia-1))*(load[j]/Capacity[keys1.index(j)] -1)
          if k <= P:
            ##enlistamos los nodos colapsados
            DELETE_NODES.append(j) 
    #se eliminan los nodos colapsados
    G.remove_nodes_from(DELETE_NODES) 
  return G,ATTACK,DAMAGE

def edge_hub_cascade_failure(G,Initial_Capacity,Resiliencia,Number_Attacks):
  """
  (Graph,float,float,int) -------> (G)
  Esta funcion ataca nodos acorde a su ranking en la medida load y luego aplica una falla en cascada
  acorde a que nodos soportan un mayor load que el dado por su capacidad inicial y resiliencia
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
  for i in range(Number_Attacks): 
    NodosBC = len(max(nx.connected_components(G), key = len))
    #registramos el daño con el cambio en el tamaño de la componente principal y los ataques
    DAMAGEEDGE.append(NodosBC/len(G.nodes()))
    ATTACK.append(i) 
    #se remueve el edge con mas load 
    edge_remove_hub_load(G,1) 
    DELETE_EDGES = []
    load = nx.edge_load_centrality(G)
    for j in G.edges():
        #calculamos el valor de load sobre el cual un nodo colapsara con 100% de seguridad
      val = Resiliencia*Capacity[keys1.index(j)] 
      #enlistamos los nodos que colapsaran con 100% de seguridad
      if load[j] > val:  
        DELETE_EDGES.append(j)
      else:
        #se elige si un nodo que ha superado su capacidad colapsa
        if load[j] > Capacity[keys1.index(j)]: 
          k = st.uniform.rvs()
          P = (1/(Resiliencia -1))*(load[j]/Capacity[keys1.index(j)] - 1)
          if k <= P:
            #enlistamos los nodos colapsados
            DELETE_EDGES.append(j) 
    #se eliminan los nodos colapsados
    G.remove_edges_from(DELETE_EDGES) 
  return G, ATTACK, DAMAGEEDGE