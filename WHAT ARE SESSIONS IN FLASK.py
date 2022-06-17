from flask import Flask, jsonify, request, url_for, redirect, session

#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"

#SESSIONS
#we will use the "home" and "json" functions to demonstrate the sessions function in flask
@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"
    session['name'] = name
    #A Session object is also a dictionary object that contains key value pairs for session variables and associated values.
    #the above code statement is used to set a name for the session which the user enters in the url
    return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

@app.route('/json')
def json():
    if 'name' in session:#checks to see if that name is present in the function
        name = session['name']#if it is present retrives it and then stores it in a json format by running the return statemnet below
    else:
        name = 'not in session'#if the name is not present then in the json function, the value given in the code would be stored

    return jsonify({'key' : 'value', 'listkey' : [1,2,3,4,5], 'name': name})#here we make a key:value pair for the name provided by the user
