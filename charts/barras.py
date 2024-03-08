import matplotlib.pyplot as plt

def plot_bar_graph(keys:list, values:list, title:str='Gráfico de Barras'):
    """
    Crea un gráfico de barras a partir de las claves y valores proporcionados.

    Argumentos:
    keys -- Lista de claves para etiquetar las barras.
    values -- Lista de valores para las alturas de las barras.
    """
    # Verificar si la cantidad de claves y valores es la misma
    if len(keys) != len(values):
        raise ValueError("La cantidad de claves y valores debe ser la misma.")

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))  # Tamaño del gráfico
    plt.bar(keys, values)  # Crear las barras
    plt.xlabel('Rating')  # Etiqueta del eje x
    plt.ylabel('VideoJuegos')  # Etiqueta del eje y
    plt.title(title)  # Título del gráfico
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para una mejor visualización
    plt.tight_layout()  # Ajustar el diseño
    plt.show()  # Mostrar el gráfico

if __name__ == '__main__':
    # Ejemplo de uso
    keys = ['A', 'B', 'C', 'D', 'E']
    values = [10, 20, 15, 25, 20]
    plot_bar_graph(keys, values)
