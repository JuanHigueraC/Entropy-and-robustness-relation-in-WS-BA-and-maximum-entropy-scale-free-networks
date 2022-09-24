#Esta funcion recibe un xfinal hasta donde sumar y un numero de particiones.
#Juntos definen la longitud y el valor maximo del vector resultante
def pareto_cumm_probabilities(particiones,xfin, alpha, distribution = st.pareto.cdf):
  """
  (particiones,xfin,alpha) -----> (probability_cum_vector)
  Esta funcion recibe un xfinal hasta donde sumar, un exponente para la ley de potencias
  y un numero de particiones. Juntos definen la longitud y el valor maximo del vector resultante.
  Entrega como resultado un vector con las probabilidades acumuladas en los puntos de las particiones
  """
  dx = (xfin-1)/particiones
  x = []
  probability_cum_vector = []
  for i in range(particiones):
    equis = 1 + dx*i
    x.append(equis)
    pes = st.pareto.cdf(x[i],alpha-1) 
    probability_cum_vector.append(pes)
  return probability_cum_vector, x # entrega como resultado el vector y los valores de x asociados

