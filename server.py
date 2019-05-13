from flask import Flask, render_template, Response,request,url_for, session, redirect, request, escape, jsonify ,send_from_directory
from flask_bootstrap import Bootstrap

from werkzeug import secure_filename
from dataPrepare import *
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
        if str(request.form.get('way')) == "1":
            return render_template('anonymizeCSV.html')
        else:
            return render_template('anonymizeDB.html')

@app.route('/anonymize/csv',methods=['POST','GET'])
def anonymizeCSV():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename("preAnonymize.csv"))
        startAnonymize()
        return send_from_directory(app.root_path, filename="Users.csv")
        # return render_template('anonymizeCSV.html', success=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True) 