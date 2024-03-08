import csv 
import matplotlib.pyplot as plt

with open('games.csv', 'r') as file:
    # Crear un lector CSV
    reader = csv.reader(file, delimiter=',')

    # Titulos
    headers = next(reader)
    # print(headers)

    # Obtener índice de la columna "Title"
    title_index = headers.index('Title')
    realese_date_index = headers.index('Release Date')

    # Obtenemos el contenido
    titles_data = [ row[title_index] for row in reader]
    realese_date = [ row[realese_date_index] for row in reader ]

    print(realese_date)
