from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField('Description of Task', validators=[DataRequired()])
    submit = SubmitField('Add the Task')