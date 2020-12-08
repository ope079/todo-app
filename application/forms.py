from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField

class BasicForm(FlaskForm):
    date_field = DateField('Enter Date')
    name_field = StringField('Enter Todo Name')
    description_field = StringField('Describe Todo')
    completed_field = SelectField('Completed', choices= [('y', 'Yes'), ('n', 'No')])
    submit = SubmitField('Submit Todo')