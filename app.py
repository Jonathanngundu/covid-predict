from flask import Flask, flash, redirect, render_template
import data


app= Flask(__name__)

us_cases = data.us_cases
sa_cases = data.sa_cases
uk_cases = data.uk_cases
us_next_week = data.us_next_week
uk_next_week = data.uk_next_week
sa_next_week = data.sa_next_week

@app.route('/')
def index():
    return render_template("index.html", uk_cases=uk_cases, us_cases=us_cases, sa_cases=sa_cases, us_next_week=us_next_week, sa_next_week=sa_next_week, uk_next_week=uk_next_week)

@app.route('/about')
def about():
    return render_template("about.html")