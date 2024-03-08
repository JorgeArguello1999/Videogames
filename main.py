# Importamos los datos 
from data.csv_read import read_data_csv

# Importamos los gráficos
from charts.barras import plot_bar_graph

def raiting(best_or_worst:bool=True, items:int=10):
    """
    best_or_worst -> True para ver los mejores, False para ver los peores
    items -> Número de items que quiere obtener
    """

    # Datos del json 
    data = read_data_csv('./data/games.csv')

    # Ordenamos por Ranking
    data.sort(key=lambda x: float(x['Rating']) if x['Rating'].strip() else 0, reverse=best_or_worst)

    # Obtenemos el número de registros
    if items <= 0: items = 1
    if items > len(data): items = len(data) 

    return [data[i] for i in range(items)]

if __name__ == '__main__':
    ## Rating
    dates = raiting(items=5, best_or_worst=True)
    # Llaves 
    keys = [data['Title'] for data in dates]
    # Valores 
    values = list(map(lambda x: float(x['Rating']) if x['Rating'].strip() else 0, dates))
    # Mostrar las estadisticas 
    plot_bar_graph(keys=keys, values=values, title='Rating')