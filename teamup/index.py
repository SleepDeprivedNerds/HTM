from flaskext.mysql import MySQL
from flask import Flask , render_template, send_from_directory, redirect, url_for , jsonify, request, session



app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'htm_teamup'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
app.secret_key = b'secret key'
#cursor = mysql.get_db().cursor()


@app.route("/")
def index():
    return render_template("home/index.html")


@app.route("/find")
def find():
    session['create']=False
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
    session['create']=True
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
    return render_template("login/index.html")


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('error/404page.html'), 404

@app.errorhandler(500)
def pageNotFound(error):
    return render_template('error/500page.html'), 500

#Form for create page thing
@app.route("/create/sendData",methods=["POST"])
def createForm():
   session['event'] = (request.form["location"],request.form["time"],request.form["description"])
   redirect(url_for(login))

#Create a post thing magic
@app.route("/login/sendData",methods=["POST"])
def checkLogin():
    # SQL check
    conn = mysql.connect()
    cursors = conn.cursor()
    auth = cursors.execute("Select * from user where password='"+request.form["password"]+"' and  username='" + request.form["username"]+"'")

    if (int(auth) == 1):
        session['auth'] = True
        if (session['create'] == True):
            write = cursors.execute("Insert into event (location,time,description) values("+session['event'][0]+"," +session['event'][1]+"," +session['event'][2])
            id = cursors.execute("Select id from event where location = {}".format(session['event'][0]))
            session['eventID'] = id
            #link to create page
            return redirect(url_for('create'))
        else:

            return redirect(url_for('viewEvent',session['event']))

    else:
        session['auth']=False



if __name__ == "__main__":
    app.run(debug=True)
