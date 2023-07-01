from flask import render_template, request, redirect, url_for
from app import app


@app.route('/')
def index():
    return 'Добро пать на главную страницу!'

