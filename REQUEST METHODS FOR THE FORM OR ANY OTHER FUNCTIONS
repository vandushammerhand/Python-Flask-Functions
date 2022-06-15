from flask import Flask, jsonify, request, url_for, redirect, session

#CONFIGURATIONS
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"

#INCOMING REQUEST METHOD
#this method will allow us to use both "GET" and other methods in the same view function/route
@app.route('/theform', methods=["GET","POST"])
def theform():
    if request.method == 'GET':
    #if statement to check if the specific condition is fulfilled or not, if the method is get then it will return the form website
       return '''<form method="POST" action="/theform">                 
                      <input type ="text" name ="name">
                       <input type ="text" name ="location">
                       <input type ="submit" name ="Submit">
                </form>'''
    else:
        #if the its a "POST" request then we will get the form values for the entered values in the form website
        name = request.form["name"]
        location = request.form["location"]
        return "Hello {}. You are from {}. Your form has been subitted successfully".format(name,location)
