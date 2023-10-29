from flask import Flask, render_template #  import Flask class

app = Flask(__name__) # helps Flask find templates static files

# List of dictionaries - dummy data
posts = [
    {
        'author': 'Terry Dutcher',
        'title': 'Blog Post 1', 
        'content': 'First Post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jacqui Ward',
        'title': 'Blog Post 2', 
        'content': 'Second Post content',
        'date_posted': 'April 21, 2018'
    }
]

# You can have multiple decorators for one function so both / and /home go to the same page
@app.route("/home")
@app.route("/") #  oreate home page route
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

