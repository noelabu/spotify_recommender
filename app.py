
#Import the libraries
from flask import Flask, request, jsonify, render_template


#Initializing the flask app
app = Flask(__name__) 

#Routing of the page 
@app.route('/')
def home():
    return render_template('index.html')


#Run!
if __name__ == "__main__":
    app.run()