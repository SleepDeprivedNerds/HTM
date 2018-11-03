from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home/index.html", name="dsad")


@app.route("/find")
def find():
    return "Find a tea place"


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
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
