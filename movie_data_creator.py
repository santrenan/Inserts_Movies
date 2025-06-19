import csv


movies = []

# Alterar nome do arquivo na hora de rodar
with open("movies_list.csv", 'r', encoding='utf-8') as csv_file: 
    reader = csv.DictReader(csv_file)
    for row in reader: # Cada row é um Dict
        movies.append(row)
    

# Cria um Insert para add no Banco de Dados (MySQL)
with open('insert_movies.sql', 'w', encoding='utf-8') as sqlfile:
    for movie in movies:
        date = movie['Date']
        name = movie['Name'].replace("'", "''")
        year = movie['Year']
        uri = movie['Letterboxd URI']

        sql = f"INSERT INTO movies_data (date, name, year, uri) VALUES ('{date}', '{name}', {year}, '{uri}');\n"
        sqlfile.write(sql)
