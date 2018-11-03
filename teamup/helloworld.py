from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home/index.html" , name="dsad")

@app.route("/find")
def find():
    return "Find a tea place"


@app.route("/create")
def createEvent():
    return "Create a Tea event"

@app.route("/event/edit/<id>")
def editEvent(id):
    return "Edit event " + str(id)


@app.route("/event/view/<id>")
def viewEvent(id):
    return "View event "+ str(id)


@app.route("/login")
def login():
    return "Login"


@app.errorhandler(404)
def pageNotFound():
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
