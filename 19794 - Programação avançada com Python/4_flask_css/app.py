from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("pagina1.html")




@app.route('/pag2')
def pag2():  # put application's code here
    return render_template("pagina2.html")



if __name__ == '__main__':
    app.run()
