from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)

#Configurations
app.config['DEBUG'] = TRUE
app.config['SECRET_KEY'] = "azyreternal"

#TEMPLATES
#to demonstrate templates we will be reusing the 'theform' and 'url' and 'redirect' functions
app.route('/theform')
def theform():
    if request.method == 'GET':
        return render_template('form.html')
        #instead of inserting the html content here along with the code statements, it would be a much morr effective way to create a template of that statement in an html file and load it in using the 'render_template' function
    else:
        name = request.form['name']
        return redirect(url_for('home', name = name))

if __name__=="__main__":
   app.run(debug=True)
   #the debug variable to bring about instant updations to the code without the need to restart the code statemets all over again
     app.run()   
         
#Rest of the functions
#TEMPLATES
#refer the html files for complete understanding
#to demonstrate the template functions, we will be reusing the 'home' and 'theform' functions  
@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return render_template('home.html',name=name, display = TRUE, nlist=['one','two','three','four','five'], nlistofdict=[{'name': 'john'},{'name':'elliot'}])
    #nlistofdict is list of dictionaries
    #the nlist is used to demonstrate loops 
    #display is an argument that is used to conduct a logical statement from the template, in this case the if statement
    #the name the user will pass through the route
    #whenever we need to pass a variable into the template by adding an argument related to the variable in the code
    #we create a new template for the home route called 'home.html', which will be returned when the home route is initialized

#Inheritances 
@app.route('/theform')
def theform():
    if request.method == 'GET':
        return render_template('inheritanceform.html')
        #instead of inserting the html content here along with the code statements, it would be a much more effective way to create a template of that statement in an html file and load it in using the 'render_template' function
    else:
        name = request.form['name']
        return redirect(url_for('home', name = name))

if __name__=="__main__":
        #app.run(debug=True)
        #the debug variable to bring about instant updations to the code without the need to restart the code statemets all over again
        app.run()   
