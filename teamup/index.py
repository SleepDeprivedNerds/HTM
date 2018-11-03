from flask import Flask , render_template, send_from_directory
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home/index.html" , name="dsad")

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
def pageNotFound(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
