from flask import Flask, jsonify, request, url_for, redirect, session
#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"


#REQUESTING FORM DATA
@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">                 
                    <input type ="text" name ="name">
                    <input type ="text" name ="location">
                    <input type ="submit" name ="Submit">
              </form>'''
              #here the action variable means that another section "process is present and that the page data is being transferred to it"
              
@app.route('/process', methods=["POST"])
def process():
    name = request.form["name"]
    #Use request. form to get data when submitting a form with the POST method. Use request. args to get data passed in the query string of the URL, like when submitting a form with the GET method.    
    location = request.form["location"]#this method only works with form data that is retrievd using the POST method
    return "Hello {}. You are from {}. Your form has been subitted successfully".format(name,location)
