from flask import Flask,render_template,redirect,url_for


# Importacions per Application
# Iniciem la APP
app = Flask(__name__)

# GLOBAL VARIABLES
# ----- FUNCTIONS ----- #

# ----- DEVELOPMENT ----- #
@app.route('/prova')
def prova():
    a = 'prova'
    return render_template("prova.html")

# ----- PRODUCCIÓ ----- #
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/demo/<code>')
def demo(code):
    
    return render_template("index.html",code=code)




# Login Stuff
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/forgot")
def forgot():
    return render_template("forgot.html")

@app.route("/register")
def register():
    return render_template("register.html")


# Ejecuta la aplicación si este archivo es el punto de entrada
if __name__ == '__main__':
    app.run(debug=True)
