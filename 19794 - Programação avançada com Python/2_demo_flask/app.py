from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ola_Mundo')
def hello_world():
    return '<h1>ola Mundo!</h1>'

@app.route('/info')
def info():
    return render_template('base.html')

@app.route('/info2')
def info2():
    return render_template('base2.html')

@app.route('/info/<usrName>')
def info_user(usrName):
        
    lst = ['item1', 'item2', 'item3']
    return render_template('base2.html', nome=usrName, lista=lst)

@app.route('/info2', methods=['POST'])
def info_post():
    return ""

if __name__ == '__main__':
    app.run()
