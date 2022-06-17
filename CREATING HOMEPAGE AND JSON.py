from flask import Flask, jsonify, request, url_for, redirect, session
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"
#Assign session IDs to sessions for each client. Session data is stored at the top of the cookie, and the server signs it in encrypted mode.
#For this encryption, the Flask application requires a defined SECRET_KEY

@app.route('/home')#here we have to type in /home to move to the next section and for the home function to run and display its contents
def home():
    return '<h1>You are in the home page</h1>'

@app.route('/json')
def json():
   return jsonify({'key' : 'value', 'listkey' : [1,2,3,4,5]})#this statement is used to convert the values to a json format
