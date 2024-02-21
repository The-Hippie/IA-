#descargar matplotlib
import matplotlib.pyplot as plt 
import numpy as np

# Pesos dados
w0 = 0
w1 = -0.5
w2 = 2

# Función para clasificar un punto usando el perceptrón dado
def clasificar_punto(x, y):
    resultado = w0 + w1*x + w2*y
    if resultado >= 0:
        return 'green'
    else:
        return 'red'

# Puntos de ejemplo de la imagen (debes reemplazar estos con las coordenadas reales)
puntos = [(9,6), (14,8), (7,9), (11,9), (8,11), (2,14), (16,5), (17,10), (19,3)]

# Clasificando cada punto y dibujando en el gráfico
for x,y in puntos:
    clasificacion = clasificar_punto(x,y)
    plt.scatter(x, y, color=clasificacion)

# Dibujar la línea divisora
x = np.linspace(0, 30, 400)
y = (-w1/w2)*x - w0/w2
plt.plot(x, y, '-r')

# Configurar los títulos y las etiquetas de los ejes
plt.title('Perceptrón')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Ajustar los límites de los ejes
plt.xlim(0, 20)
plt.ylim(0, 20)

# Mostrar el gráfico
plt.show()