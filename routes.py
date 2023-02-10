from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route("/index")
def index():
    user = {'username': 'Артем', 'age': '13'}
    posts = [
        {
        'author': {'username': 'Denys', 'age':'14'},
        'body': 'Живіть, як хочете!!'
        },
        {
            'author': {'username': 'Kirill', 'age': '13'},
            'body': 'Задачі нас не пугають, вони нас озадачують'
        }
    ]
    return render_template("index.html", title="Home", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember me = {form.remember_me.data}')
        return redirect(url_for("index"))
    return render_template("login.html", title="sign in", form=form)

    return render_template("login.html", foorm=frm)

#@app.route("/register")
#def register():
    #form = RegistrationForm()
    #if form.validate_on_submit():
        #flash(f'Login requested for user {form.username.data}, remember me = {form.remember_me.data}')
       # return redirect(url_for("index"))
    #return render_template("register.html", title="sign in", form=form)

@app.route("/other")
def other():
    return render_template("other.html", title="Інше про")

@app.route("/create-post")
def create_post():
    return render_template("create-post.html")



