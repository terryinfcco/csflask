from flask import Flask #  import Flask class

app = Flask(__name__) # helps Flask find templates static files

# You can have multiple decorators for one function so both / and /home go to the same page
@app.route("/home")
@app.route("/") #  oreate home page route
def hello():
    return 'Hello World!'

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)

