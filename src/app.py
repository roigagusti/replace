from flask import Flask,render_template,redirect,url_for,request
from werkzeug.utils import secure_filename
from classes.demo import Demo, replace
from classes.legal import Legal
import os


# Importacions per Application
# Iniciem la APP
app = Flask(__name__)
UPLOAD_FOLDER = 'static/import'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Instanciem serveis
dm = Demo()
dm.create_demo_token()


# GLOBAL VARIABLES
# ----- FUNCTIONS ----- #
      
# ----- DEVELOPMENT ----- #
@app.route('/prova')
def prova():
    a = 'prova'
    return render_template("prova.html")

# ----- PRODUCCIÓ ----- #
# SITE #
@app.route('/')
def index():
    token = dm.token
    return render_template("www/index.html",token=token)

@app.route('/demo/<token>', methods=['GET', 'POST'])
def demo(token):
    if token == dm.token:
        data_raw = request.form.items()
        data_received = dm.receive_multiple_inputs(data_raw)
        print(data_received)
        file = request.files['wordfile']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        output = replace(data_received, filename)           
        return output 
    else:
        print('Token incorrecte')
        return redirect(url_for('index')) 
    
@app.route('/legal/<page>', methods=['GET', 'POST'])
def legal(page):
    lg = Legal(page)
    return render_template("www/legal.html",title=lg.title,date=lg.date,text=lg.text)
 
# APP #
@app.route('/app/', methods=['GET', 'POST'])
def app_index():
    return redirect(url_for('app_templates'))

@app.route('/app/templates', methods=['GET', 'POST'])
def app_templates():
    return render_template("app/templates.html")

@app.route('/app/templates/<code>', methods=['GET', 'POST'])
def app_templates_detail(code):
    return render_template("app/template-detail.html",code=code)

@app.route('/app/variables', methods=['GET', 'POST'])
def app_variables():
    return render_template("app/variables.html")
    



# Login Stuff
@app.route("/login")
def login():
    return render_template("app/login.html")

@app.route("/forgot")
def forgot():
    return render_template("app/forgot.html")

@app.route("/register")
def register():
    return render_template("app/register.html")

@app.route("/logout")
def logout():
    return "Fora"


# Ejecuta la aplicación si este archivo es el punto de entrada
if __name__ == '__main__':
    app.run(debug=True)
