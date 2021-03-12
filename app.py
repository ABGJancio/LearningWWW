from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/mypage/me')
def about_me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def send_message():
    if request.method == 'GET':
        print("We received GET")
        return render_template("contact.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/mypage/me")
