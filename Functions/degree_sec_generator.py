#Este algoritmo es para muestrar secuencias de enteros on una distribucion dada. (Montecarlo
def Degree_Sec_Generator(Probabilidad_Acumulada,longitud_Secuencia,kmin):
  """
  (Vector Probabilidada Acumulada, Longitud Secuencia,kmin) -------> (Secuencia de enteros con la distribucion del vector)
  Este algoritmo es para muestrar secuencias de enteros con una distribucion de ley de potencias con exponente entre 2 y 3. (Montecarlo)
  recuerde que si quiere una secuencia de grado longitud_Secuencia = len(Probabilidad_Acumulada)
  kmin corresponde al valor minimo desde el cual se muestreará la distribucion, si no es necesario poner 0.
  """
  Degree_Sequence = []
  sum = 0
  #por la condicion del cutoff no todos los enteros son aceptados, por lo cual se hacen 100000 intentos, para asegurar
  # que se encuentre la distribucion de grado de la longitud requerida
  intentos = 10000*longitud_Secuencia
  for i in range(intentos):
    k = np.random.rand()*Probabilidad_Acumulada[len(Probabilidad_Acumulada)-1]
    for j in range(len(Probabilidad_Acumulada)): 
    #la siguiente condicion busca la posicion en el vector de probabilidades acumuladas que es justo mayor
    # que el numero extraido aleatoriamente, para asi tomar el numero de esta posicion como un grado de la secuencia
      if k <= Probabilidad_Acumulada[j]: 
          #la siguiente condicion solo acepta el entero si es menor que el cutoff
        if j <= round(len(Probabilidad_Acumulada)**(1/2) + 10): 
          Degree_Sequence.append(j+kmin-1) 
          break
    #cuando la longitud de la secuencia sea la longitud requerida rompe
    if len(Degree_Sequence) == longitud_Secuencia:
      break
  return Degree_Sequence
