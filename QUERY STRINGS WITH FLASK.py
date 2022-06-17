import from flask import Flask, jsonify, request, url_for, redirect, session

#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"

#QUERY STRINGS
@app.route('/query')#creating a route query
def query():#creating a function that runs when prequisite value is entered by the user
    name= request.args.get('name')
    #code to get the name value from the user as a multi dictionary
    
    location= request.args.get('location')
    return '<h1>Hello {}. Your are from {}. You are on the query page!</h1>'.format(name,location)
    
#When the code is run, we will move to the website where the user will have to make certain changes in the url to get the name and location
# "http://127.0.0.1:5000/query?name=Guillman&location=Ultramar" - here the user will have to type in the part - "/query?name=Guillman&location=Ultramar", so as to get the name and location values which would then be displayed in the website
# "/query?name=Guillman&location=Ultramar" - everything after the question mark is the string query and to start a query, user has to input a "?" to start the query
