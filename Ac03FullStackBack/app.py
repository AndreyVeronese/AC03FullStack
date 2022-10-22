from flask import Flask, request

import json
app = Flask(__name__)
@app.route('/Cadastro/Aluno', methods = ['POST'])
def cadastrar_aluno():
    tasks = [
        {
            "ra": 2100667,
            "name": "Emmanuel",
            "curso": "Analise e desenvolvimento de sistemas"

        },
        {
            "ra": 2100666,
            "name": "Fulano",
            "curso": "Analise e desenvolvimento de sistemas"
        }
    ]
    tasksJSON = json.dumps(tasks)
    return tasksJSON