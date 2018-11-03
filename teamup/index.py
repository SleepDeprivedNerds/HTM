from flask import Flask , render_template, send_from_directory, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home/index.html", name="dsad")


@app.route("/find")
def find():
    return "Find a tea place"

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/fonts/<path:path>')
def send_font(path):
    return send_from_directory('fonts', path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route("/create")
def createEvent():
    return "Create a Tea event"


@app.route("/event/edit/")
@app.route("/event/edit/<ident>")
def editEvent(ident=None):
    if ident is not None:
        return "Edit event " + str(ident)
    return redirect(url_for('index'))


@app.route("/event/view/")
@app.route("/event/view/<id>")
def viewEvent(ident=None):
    if ident is not None:
        return "View event " + str(ident)
    return redirect(url_for('index'))


@app.route("/login")
def login():
    return "Login"


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('error/404page.html'), 404

@app.errorhandler(500)
def pageNotFound(error):
    return render_template('error/500page.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
