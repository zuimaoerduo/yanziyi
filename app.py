from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/about.html')
def about():  # put application's code here
    return render_template("about.html")


@app.route('/services.html')
def services():  # put application's code here
    return render_template("services.html")

@app.route('/blog.html')
def blog():  # put application's code here
    return render_template("blog.html")

@app.route('/blogsingle.html')
def blogsingle():  # put application's code here
    return render_template("blogsingle.html")

if __name__ == '__main__':
    app.run()
