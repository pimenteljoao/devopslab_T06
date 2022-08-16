from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():

    return "Alteração da mensagem original recuperei as aulas de sábado"

if __name__ == '__main__':
    app.run()
