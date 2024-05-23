from flask import Flask, render_template, url_for, request
from datetime import datetime
import pandas as pd


app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/Menu", methods=['POST'])
def Menu():
    return render_template("Menu.html")

@app.route("/Adm", methods=['POST'])
def Adm():
    dados_html = ler_planilha_excel('A')
    return render_template('Adm.html', dados_html=dados_html)
    #return render_template('Adm.html')

@app.route("/Info", methods=['POST'])
def Info():
    dados_html = ler_planilha_excel('I')
    return render_template('Info.html', dados_html=dados_html)
    #return render_template("Info.html")

@app.route("/Bibli", methods=['POST'])
def Bibli():
    dados_html = ler_planilha_excel('B')
    return render_template('Bibli.html', dados_html=dados_html)
    #return render_template("Bibli.html")

@app.route("/Multi", methods=['POST'])
def Multi():
    dados_html = ler_planilha_excel('M')
    return render_template('Multi.html', dados_html=dados_html)
    #return render_template("Multi.html")



def ler_planilha_excel(bloco):
    try:
        dia_atual = datetime.today().weekday()


        dados = pd.read_excel('/workspaces/codespaces-flask/dados.xlsx', sheet_name=bloco)

        dados_excel = dados.fillna('')
        dados_filtrados = dados_excel[dados_excel['Dia'] == dia_atual]
        dados_final = dados_filtrados.drop('Dia', axis=1)


        tabela_html = dados_final.to_html(index=False)
        


        tabela_html_com_estilos = """ <html>
          <head> 
            <style> 
            /* Estilos para as células */ 
            td { border: 1px solid black;

            /* Borda das células */ 
            padding: 5px;

            /* Espaçamento interno das células */

            /* Centraliza o texto */
            text-align: center; 
            td, th { 
                border: 1px solid black;
                /* Borda das células */ 
                padding: 5px;
                /* Espaçamento interno das células */
                text-align: center; /* Centraliza o texto nas células */
} 

            } 
            /* Estilos para células vazias */ 

            td:empty { background-color: lightgreen; 
            /* Cor de fundo das células vazias */ 
            } 
            
            /* Estilos para a primeira linha da tabela */ 
            tr:first-child { background-color: lightgrey; 
             text-align: center;
            /* Cor de fundo da primeira linha */ 
            
            } 
            </style> 
          </head> 
          <body> 
          """ + tabela_html + """ 
          </body> 
          </html> """


        
        return tabela_html_com_estilos
    
    except Exception as e:
        return f"Ocorreu um erro ao ler a planilha: {e}"

    

if __name__ == '__main__':
    app.run(debug=True)