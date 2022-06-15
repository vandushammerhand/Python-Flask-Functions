from flask import Flask, jsonify, request, url_for, redirect, session

#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"

#REDIRECTS AND URL_FOR
#assume we are redirecting the user to the homepage after successful form submission

@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, you are on the home page!</h1>'.format(name)


@app.route('/theform', methods=["GET","POST"])
def theform():

    if request.method == 'GET':
        return '''<form method="POST" action="/theform">                 
                        <input type ="text" name ="name">
                        <input type ="text" name ="location">
                        <input type ="submit" name ="Submit">
                </form>'''
    else:
        name = request.form['name']
        return redirect(url_for('home', name = name))
#we are able to add other values as well in the "url_for" function like the location, but since it has not been initialized in the home function, it will be shown as a query string in the url of the home page
#the "name = name", part is used to show the user inputed name in the home page, the name that the user entered in the form page 
#this is the code statement that will redirect the user to the homepage, we put the function in the "url_for" function and not the route itself
