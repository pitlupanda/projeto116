#Importando o módulo flask no projeto
from flask import Flask, render_template

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe  Flask
@app.route("/")

# A URL ‘/’ é ligada à função first_flask.
def first_flask():

    return "Este é meu primeiro programa Flask"
@app.route("/Flask")
def second_flask():
    return "python é divertido"
@app.route("/index")
def first_webpage():
    name = 'pedro'
    name2 = 'henrique'
    return render_template('index.html', student_name = name, index_variable=name2)

# Execute a aplicação no servidor local
app.run()
