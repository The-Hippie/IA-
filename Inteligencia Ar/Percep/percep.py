#descargar matplotlib
import matplotlib.pyplot as plt 
import numpy as np

# Pesos dados
w0 = 0
w1 = -0.5
w2 = 2

# Función para clasificar un punto usando el perceptrón dado
def clasificar_punto(y, x):
    resultado = w0 + w1*y + w2*x
    if resultado >= 0:
        return 'green'
    else:
        return 'red'

# Puntos de ejemplo de la imagen (debes reemplazar estos con las coordenadas reales)
puntos = [(9,6), (14,8), (7,9), (11,9), (8,11), (2,14), (5,16), (10,17), (3,19)]

# Clasificando cada punto y dibujando en el gráfico
for x,y in puntos:
    clasificacion = clasificar_punto(y,x)
    plt.scatter(y, x, color=clasificacion)
    if clasificacion == 'red':
        plt.plot([0, y], [x, x], 'r--') # línea horizontal hasta el eje Y
        plt.plot([y, y], [0, x], 'r--') # línea vertical hasta el eje X
    elif clasificacion == 'green':
        plt.plot([0, y], [x, x], 'g--') # línea horizontal hasta el eje Y
        plt.plot([y, y], [0, x], 'g--') # línea vertical hasta el eje X

# Dibujar la línea divisora
x = np.linspace(0, 50, 100)
y = (-w1/w2)*x - w0/w2
plt.plot(x, y, '-r')

# Configurar los títulos y las etiquetas de los ejes
plt.title('Perceptrón')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Ajustar los límites de los ejes
plt.xlim(0, 20)
plt.ylim(0, 15)

# Cambiar el incremento de los ejes a una unidad
plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(0, 16, 1))

# Mostrar el gráfico
plt.show()
