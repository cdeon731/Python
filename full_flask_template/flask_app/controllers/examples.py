from flask_app.models.#model_file_name import #model
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# app.routes go here