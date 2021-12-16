from app import app

from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/docs')
def docs():
    return render_template("swaggerui.html")


@app.route('/signIn',methods=["GET","POST"])
def sign_in():
    return render_template('sign_in.html')

shop_items = [
    {
        'title':'Item title 1',
        'text':'Item text 1'
    },
    {
        'title':'Item title 2',
        'text':'Item text 2'
    },
    {
        'title':'Item title 3',
        'text':'Item text 3'
    },
    {
        'title':'Item title 4',
        'text':'Item text 4'
    },
    {
        'title':'Item title 4',
        'text':'Item text 4'
    },
    {
        'title':'Item title 4',
        'text':'Item text 4'
    },
    {
        'title':'Item title 4',
        'text':'Item text 4'
    },
    {
        'title':'Item title 4',
        'text':'Item text 4'
    }
]

@app.route('/shop')
def shop():
    return render_template("shop.html",items=shop_items)