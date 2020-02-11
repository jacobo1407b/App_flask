from flask import Flask, jsonify, request, url_for, redirect, session

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']='mysecretapp'

@app.route('/')
def index():
    return jsonify({'estado':'correcto'})
