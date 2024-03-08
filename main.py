# Importamos los datos 
from data.csv_read import read_data_csv

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
    dates = raiting(items=2, best_or_worst=False)
    print(dates)