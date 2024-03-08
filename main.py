# Importamos los datos 
from data.csv_read import read_data_csv

data = read_data_csv('./data/games.csv')
print(data)


if __name__ == '__main__':
    pass