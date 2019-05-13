from flask import Flask, render_template, Response,request,url_for, session, redirect, request, escape, jsonify ,send_from_directory
from flask_bootstrap import Bootstrap

from werkzeug import secure_filename
from dataPrepare import *
from config import *

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anonymize/')
def anonymize():
    return render_template('anonymize.html')

@app.route('/anonymize',methods=['POST','GET'])
def getWayToAnonymize():
    # if request.method == 'POST':
        if str(request.form.get('way')) == "csv":
            return render_template('anonymizeCSV.html')
        else:
            return render_template('anonymizeDB.html')

@app.route('/anonymize/csv',methods=['POST','GET'])
def anonymizeCSV():
    if request.method == 'POST':
        table_name  = request.form.get('table_name')
        f           = request.files['file']
        f.save(secure_filename("preAnonymize.csv"))

        df = read_from_csv(csv_path)
        startAnonymize(df , table_name)
        return send_from_directory(app.root_path, filename = table_name + ".csv")

@app.route('/anonymize/db',methods=['POST','GET'])
def anonymizeDB():
    if request.method == 'POST':
        host        = request.form.get('host')
        user        = request.form.get('user')
        password    = request.form.get('password')
        database    = request.form.get('database')
        table_name  = request.form.get('table_name')

        df = read_from_db(host, user, password, database , table_name)
        startAnonymize(df, table_name)
        return send_from_directory(app.root_path, filename=table_name + ".csv")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)