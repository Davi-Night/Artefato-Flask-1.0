from flask import Flask, render_template, url_for, request
from datetime import datetime
import pandas as pd
from pytz import timezone
import pytz


app = Flask(__name__)


#Pagina de Login
@app.route("/")
def login():
    return render_template("login.html")

#Seletor de Bloco
@app.route("/Menu", methods=['POST'])
def Menu():
    return render_template("Menu.html")

#Dados do Bloco Adm
@app.route("/Adm", methods=['POST'])
def Adm():
    dados = ler_planilha_excel('A')
    hora_atual = datetime.now(timezone('America/Sao_Paulo')).strftime("%H")
    hora_atual = int(hora_atual)
    return render_template('Adm.html', dados=dados, hora=hora_atual)

#Dados do Bloco Info
@app.route("/Info", methods=['POST'])
def Info():
    dados = ler_planilha_excel('I')
    hora_atual = datetime.now(timezone('America/Sao_Paulo')).strftime("%H")
    hora_atual = int(hora_atual)
    return render_template('Info.html', dados=dados, hora=hora_atual)

#Dados do Bloco Biblioteca
@app.route("/Bibli", methods=['POST'])
def Bibli():
    dados = ler_planilha_excel('B')
    hora_atual = datetime.now(timezone('America/Sao_Paulo')).strftime("%H")
    hora_atual = int(hora_atual)
    return render_template('Bibli.html', dados=dados, hora=hora_atual)

#Dados do Bloco Biblioteca
@app.route("/Multi", methods=['POST'])
def Multi():
    dados = ler_planilha_excel('M')
    hora_atual = datetime.now(timezone('America/Sao_Paulo')).strftime("%H")
    hora_atual = int(hora_atual)
    return render_template('Multi.html', dados=dados, hora=hora_atual)

class Sala:
    def __init__(self, dia: int, curso: str, sala: int, hora: list[str]):
        self.dia = dia
        self.curso = curso
        self.sala = sala
        self.hora = hora


def ler_planilha_excel(bloco):
    try:
        dia_atual = datetime.today().weekday()
        
        salas = []


        dados = pd.read_excel('/workspaces/codespaces-flask/dados.xlsx', sheet_name=bloco)

        dados_excel = dados.fillna('Livre')
        dados_filtrados = dados_excel[dados_excel['Dia'] == dia_atual]
        dados_filtrados = dados_filtrados[dados_excel['CURSO'] != 'Livre']
        #dados_final = dados_filtrados.drop('Dia', axis=1)

        for index, row in dados_filtrados.iterrows():

            dia = row['Dia']
            curso = row['CURSO']
            sala = row['SALA']
            hora = [
                row['08:00-10:00'],
                row['10:00-12:00'],
                row['14:00-16:00'],
                row['16:00-18:00'],
                row['18:00-20:00'],
                row['20:00-22:00']
            ]
            
            # Criar uma instância de Sala
            nova_sala = Sala(dia, curso, sala, hora)
            salas.append(nova_sala)
        
        return salas
    
    except Exception as e:
        return f"Ocorreu um erro ao ler a planilha: {e}"

    

if __name__ == '__main__':
    app.run(debug=True)