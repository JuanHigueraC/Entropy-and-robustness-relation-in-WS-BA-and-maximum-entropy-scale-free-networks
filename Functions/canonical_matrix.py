#Esta funcion recibe un vector con los multiplicadores de lagrange (ordenados de tal manera que el grado correspondiente como ligadura este ordenado de menor a mayor)
#Entrega una lista de listas con las componentes de la matriz de adyacencia promedio segun el ensamble canonico
def canonical_matrix(Multiplicadores_Lagrange):
  #se genera la lista de listas
  Adyacencia_promedio = []
  for i in range(len(Multiplicadores_Lagrange)):
    # se agrega una fila/lista por cada multiplicador
    Adyacencia_promedio.append([])
    for j in range(len(Multiplicadores_Lagrange)):
      Adyacencia_promedio[i].append(1/(1 + math.exp((Multiplicadores_Lagrange[i] + Multiplicadores_Lagrange[j]))))
  #ahora nos aseguramos que no haya autoloops
  for i in range(len(Multiplicadores_Lagrange)):
    Adyacencia_promedio[i][i] = 0
  return Adyacencia_promedio  
