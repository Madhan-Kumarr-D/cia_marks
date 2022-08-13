from flask import Flask, flash, request, redirect, url_for, render_template
import backend
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/userinput")
def userinput():
    return render_template("userinput.html")
