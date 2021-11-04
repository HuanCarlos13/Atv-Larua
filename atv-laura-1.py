import csv
from flask import Flask

app = Flask(__name__)


@app.route('/<id>', methods=['GET'])
def busca(id):
    with open('musicas.csv', encoding='utf-8') as musicas:
        table = csv.reader(musicas, delimiter=',')
        for line in table:
            if line[0] == id:
                musicas = {
                    "id": line[0],
                    "autor": line[1],
                    "faixas": line[2]
                }

                return musicas
        
        return "musica não encontrada"



@app.route('/add', methods=['POST'])
def addmusica():
    with open('Musica.csv','a' newline='') as musicas:
        writer = csv.writer(musicas, delimiter=',')
        musica = request.json

    
        musica_added = [musica['id'], musica['autor'], musica['faixas']]
        writer.writerow(musica_added)

    return 'OK'


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    with open('musica.csv', encoding='utf-8') as musicas:
        reader = csv.reader(musicas, delimiter=',')
        data = list(reader)
    
    with open('musica.csv', newline='') as musicas:
        writer = csv.writer(musicas, delimiter=',')

        for item in data:
            musicaid, autor, faixas = item

            if musicaid != id:
                writer.writerow(item)
    
    return 'OK'