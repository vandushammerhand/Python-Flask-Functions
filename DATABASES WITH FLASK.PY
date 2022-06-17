from flask import Flask, jsonify, request, url_for, redirect, session, g, render_template
import sqlite3
#What is 'g' object in Flask?
#g is an object provided by Flask. It is a global namespace for holding any data you want during a single app context. 
# For example, a before_request handler could set g. user , which will be accessible to the route and other functions. 
#forconnecting databases we will be importing 'sqlite3' to the databases file

app = Flask(__name__)

#Configurations
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "azyreternal"

#function to provide the connection between the app and the database
def connect_db(): 
    #to establish the connection we create a new variable 'sqlconnect', and provide the connection command 'sqlite3.connect' and then provide the directory within which the database is located.
    sqlconnect = sqlite3.connect('/C:/Users/Rohit/Documents/sqlite/firstdata.db')
    #here we are converting the tuples data which would be default representation of the data  in the database into python dictionaries
    #By adding 'sqlite3.Row' to row_factory
    sqlconnect.row_factory = sqlite3.Row
    return sqlconnect

#function to get the database values 
def get_db():
    #we are checking to see if the database exists or not, by checking if the file selected has the 'sqlite' attribute
    if not hasattr(g, 'sqlite_db'):
        #if the it does not have the attribute then we create the database 
        g.sqlite_db = connect_db()
    return g.sqlite_db

#function to close the connection to the database after every route gets completed
#for this we will have to create a new route that is called automatically after each round
@app.teardown_appcontext
def close_db(error):
    #checks if there exists the given attribute  
    if hasattr(g, 'sqlite_db'):
        #if the attribute exists then close the connection using 'sqlite_db.close()'
        g.sqlite_db.close()

@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello, World!</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    #to get all the values of the database showcased in the homepage
    #get the database
    db = get_db()
    #creating a cursor to direct to the output
    cursor2 = db.execute('select id, name, location from user')
    #to get the desired output
    result2 = cursor2.fetchall()
    #now to finally render it in to the template of the homepage
    return render_template('databaseshome.html', name=name, display=False, \
        nlist=['one', 'two', 'three', 'four'], nlistofdict=[{'name' : 'Zach'}, {'name' : 'Zoe'}], results = result2)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'NotinSession!'
    return jsonify({'key' : 'value', 'listkey' : [1,2,3], 'name' : name})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)
#to insert data into the database we will be modifying the 'form' route
@app.route('/theform', methods=['GET', 'POST'])
def theform():

    
    if request.method == 'GET':
        return render_template('inheritanceform.html')
    else:
        name = request.form['name']
        location = request.form['location']
        #first we get the database
        #then we provide the insert command, we require no cursor since we're not returning any data but inserting it
        db = get_db()
        #the reason why we use ? in values is to prevent sql injections, in this way sqlite can just format the insert statement by itself instead of you manually entering the values in the statement, you only need to provide a list of values in the form you want them entered
        db.execute('insert into user (name, location) values (?, ?)', [name, location])
        db.commit()

        #return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)
        return redirect(url_for('home', name=name, location=location))

@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result' : 'Success!', 'name' : name, 'location' : location, 'randomkeyinlist' : randomlist[1]})

#create a route to showcase the results from the database
@app.route('/viewresults')
def viewresults():
    #the below code is used to get the database to the new variable 'database' by using the 'get_db()' method
    database=get_db()
    #we create a cursor to point towards the result
    cursor = database.execute('select id, name, location from user')
    #to get the results we will call the cursor by using the "fetchall()" method, and the results would be a list of dictionaries
    results = cursor.fetchall()
    #each item in the list would be representing a row and each key in the dictionary would be representing a column
    #now to get the actual results we have to use the return function
    return '<h1> The Id is {}. The Name is {}. The Location is {}. </h1>'.format(results[2]['id'], results[2]['name'], results[2]['location'])


if __name__ == '__main__':
                app.run()
