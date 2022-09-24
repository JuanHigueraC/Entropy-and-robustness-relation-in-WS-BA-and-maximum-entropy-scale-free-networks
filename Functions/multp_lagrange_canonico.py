# este programa te calcula los multiplicadores de lagrange dada una secuencia de grado acorde al ensamble canonico.
def multp_lagrange_canonico(degree_sequence):
  """
  (degree_sequence) ----> (lagrange_multiplicators_canonicalensemble)
  esta funcion te recibe una secuencia de grado, te la impone como ligadura en un ensamble canonico de grafos simples y 
  te entrega un vector con los multiplicadores de lagrange ordenados de menor a mayor acorde al grado de la restricción asociada 
  """
  #la siguiente funcion contiene el sistema de ecuaciones y se define para solucionar
  def lagrange_eq(lagrange_multiplicators, degree_sequence):
    n = len(degree_sequence)
    matrix = np.zeros((n,n))
    for i in range(n):
      for j in range(n):
        #esta es la expresion de la matriz de adyacencia promedio segun el ensamble canonico
        matrix[i][j] = 1/(math.exp(lagrange_multiplicators[i] + lagrange_multiplicators[j]) + 1)
      matrix[i][i] = 0
    sums = []
    for i in range(n):
      sum = 0
      for j in range(n):
        sum = sum + matrix[i][j]
      sums.append(sum)
    resultado = np.zeros(n)
    for i in range(n):
      resultado[i] = sums[i] - degree_sequence[i] 
    return resultado

  x0 = np.zeros(len(degree_sequence))
  def lagrange(lagrange_multiplicators):
    k = lagrange_eq(lagrange_multiplicators,degree_sequence)
    return k
  #hasta aca lo que se ha hecho es definir las funciones a resolver acorde a los resultados del ensamble canonico 
  #la siguiente linea resuelve el sistema de ecuaciones y entrega el resultado en una lista
  multiplicators = fsolve(lagrange,x0) 
  return multiplicators

