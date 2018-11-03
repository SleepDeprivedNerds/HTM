import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name):
    return flask.render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()
