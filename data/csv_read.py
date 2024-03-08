import csv

def read_data_csv(path:str="./games.csv"):
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=",")

        # Cabeceras
        header = next(reader)

        # Unimos los datos
        data = []
        for row in reader:
            item = zip(header, row)
            item_dict = {key: value for key, value in item}
            data.append(item_dict)
        
        return data

if __name__ == "__main__":
    output = read_data_csv()
    print(output[0])