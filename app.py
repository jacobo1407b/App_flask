from flask import Flask, jsonify, request, url_for, redirect, session
from flask_cors import CORS
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)
CORS(app)
app.config['MONGOALCHEMY_DATABASE'] = 'NOTASXD'
db = MongoAlchemy(app)

app.config['DEBUG']=True
app.config['SECRET_KEY']='mysecretapp'

class Book(db.Document):
    titulo = db.StringField()
    descripcion = db.StringField()


@app.route('/')
def index():
    return jsonify({'estado':'correcto'})


@app.route('/newn', methods=['POST'])
def newn():
    print (request.get_json())
    data = request.get_json()
    titulo = data['titulo']
    des = data['des']
    dive = Book(titulo=titulo, descripcion=des)
    dive.save()
    return jsonify({'estado':'guardado'})


@app.route('/delete', methods=['DELETE'])
def delete():
    return jsonify({'estado':'borrado'})

#mostrar de a putaso
@app.route('/allr', methods=['GET'])
def allr():
    datos=Book.query.all()
    print (datos)
    return jsonify({'estado':datos})

@app.route('/update/<id>', methods=['PUT'])
def update(id):
    book = Book.query.get(id)
    data = request.get_json(document=book)
    data.save()
    return jsonify({'estado':'update'})


if __name__ == '__main__':
    app.run()