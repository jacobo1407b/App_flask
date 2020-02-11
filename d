@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'
@app.route('/home', methods=['GET'], defaults={'name':''})
@app.route('/home/<name>', methods=['GET'])
def home(name):
    return '<h1>Este {}es el home</h1>'.format(name)
@app.route('/json')
def json():
    return jsonify({'key':'value1', 'listen':'5000'})

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/data">
                 <input type="text" name="name" placeholder="name">
                <input type="submit" value="submit">
              </form>'''
#ddff
@app.route('/data', methods=['POST'])
def data():
    name = request.form['name']
    return jsonify({'name':name})


@app.route('/processjson', methods=['POST'])
def processjson():

    dat = request.get_json()

    name = dat['name']
    location = dat['location']

    randomlist = dat['randomlist']

    return jsonify({'result' : 'Success!', 'name' : name, 'location' : location, 'randomkeyinlist' : randomlist[1]})
