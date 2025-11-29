from flask import Flask 
app = Flask(__name__)  

@app.route("/")
def home():
    return"""
    <h1>  Home page </h1>
    <h2> I am running in Flask,very exciting</h2>
    """

@app.route("/about")
def about():  
    return"""
    <h1> about page </h1>
    <h2> I am running in Flask</h2>
    <h3> thank you for visiting </h3>
    """

if __name__=='__main__':
    app.run(debug=True)