from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"

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




if __name__ == "__main__":
    app.run()
