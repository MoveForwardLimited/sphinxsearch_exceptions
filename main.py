from flask import Flask, request, render_template, url_for, jsonify, json
from flask_mysqldb import MySQL
import exceptionLib
import settings


app = Flask(__name__)
app.config['MYSQL_HOST'] = settings.MYSQL_HOST
app.config['MYSQL_USER'] = settings.MYSQL_USER
app.config['MYSQL_PASSWORD'] = settings.MYSQL_PASSWORD
app.config['MYSQL_DB'] = settings.MYSQL_DB

exceptionLib.database = MySQL(app)

exceptionLib.loadException()

@app.route('/')
def root():
    return render_template('home.html', exceptionList=exceptionLib.exceptionList)

@app.route('/save')
def tmpSave():
    exceptionLib.saveException()
    return 'ok'

@app.route('/add', methods=['GET'])
def add():
    return render_template('addNew.html')

@app.route('/add/<key>', methods=['GET'])
def addKey(key):
    item=exceptionLib.exceptionList[key]
    return render_template('add.html', item=item, key=key)

@app.route('/search', methods=['GET'])
def searchException():
    return render_template('search.html')



@app.route('/api/list')
def list():
    return jsonify(exceptionLib.exceptionList)

@app.route('/api/search', methods=['POST'])
def search():
    try:
        request_data = request.json
        pattern=request_data['pattern']
        searchFor=request_data['for']
        res=exceptionLib.search(pattern,searchFor)
        return jsonify(res)
    except Exception as error:
        return jsonify(str(error))

@app.route('/api/view', methods=['POST'])
def save():
    try:
        request_data = request.json
        base=request_data['base']
        lista=request_data['list']
        item = exceptionLib.addExcepion(base, lista)
        exceptionLib.saveException()
        return jsonify(item)
    except Exception as error:
        return jsonify(error)
    

@app.route('/api/view/<base>', methods=['GET'])
def view(base):
    item=exceptionLib.exceptionList[base]
    return jsonify(item)

@app.route('/api/delete/<base>', methods=['GET'])
def deleteBase(base):
    res=exceptionLib.removeException(base)
    exceptionLib.saveException()
    return jsonify(res)

@app.route('/api/reload', methods=['GET'])
def reload():
    exceptionLib.reload()
    return jsonify({"msg":"ok"})

@app.route('/api/publish', methods=['GET'])
def publish():
    res=exceptionLib.publishException()
    return jsonify(res)

@app.route('/api/published')
def isUnpublished():
    return jsonify(exceptionLib.isPublished())

if __name__=='__main__':
    app.run(host='localhost', port=5000)
