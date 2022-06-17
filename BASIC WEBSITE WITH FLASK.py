from flask import Flask, jsonify, request, url_for, redirect, session
# url_for - Generates a URL to the given endpoint with the method provided.
app = Flask(__name__)

#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"
#Assign session IDs to sessions for each client. Session data is stored at the top of the cookie, and the server signs it in encrypted mode.
#For this encryption, the Flask application requires a defined SECRET_KEY

 
@app.route('/<name>')
#the route function is used to provide a way for user input to change between sections of the app as can be seen below
def index(name):
# here we create an index function based on the name the user will provide in the url and that name will be displayed in the placeholder "{}" in the below code
    return '<h1>Hello {}!</h1>'.format(name)
    #The format() method formats the specified value(s) and insert them inside the string's placeholder.
#The placeholder is defined using curly brackets: {}.

