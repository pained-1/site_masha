from flask import Flask, render_template, request, redirect, abort, send_file, url_for, flash, app
import os
app = Flask(__name__, static_folder='static')

@app.route('/')
def about():
    return render_template('base.html')
@app.route("/2")
def computer():
    return render_template("main.html")
@app.route("/3")
def stranitse():
    return render_template("formi na stranitse.html")
@app.route("/4")
def software():
    return render_template("software.html")
@app.route("/5")
def stranits2e():
    return render_template("text na stranitse.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5080))
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)
