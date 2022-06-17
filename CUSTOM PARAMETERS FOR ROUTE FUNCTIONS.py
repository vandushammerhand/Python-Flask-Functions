
from flask import Flask, jsonify, request, url_for, redirect, session

#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal


#custom input paramters for the route function

@app.route('/home', methods=['POST','GET'], defaults={'name' : 'Guest'})
#this statement is used to provide a default value for the site, so if the user enters site in the url it will show the value "Guest" as its default value, if no other value is entered

@app.route('/home/<name>')
#here we run the url based on the name that is inputed by the user "<name>" a variable like this means user input is required 

def home(name):#the same variable have to used to set the parameters, otherwise an error will occur
    return '<h1>Hello {}, you are on the home page</h1>'.format(name)#we will have to use the format function to format the values into the placeholder "{}"
#there is the option to bring about datatype changes in the user input variables, for example "<integer:name>", means that the name entered has to of integer type, otherwise an error will occur
