from flask import Blueprint, render_template, request, flash, jsonify, Flask, request
import flask
import json
from datetime import datetime, date, timedelta
from flask_cors import CORS

views = Blueprint('views', __name__)

## Home/Landing page**********************************************************************************************************************************************

@views.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST': 
        note = request.form.get('note')# Gets the note from the HTML 
        flash('Note added!', category='success')
    return render_template("home.html")

##*****************************************************************************************************************************************************************