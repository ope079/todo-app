from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class TaskForm(FlaskForm):
    description = StringField('Description of Task', validators=[DataRequired()])
    complete = SelectField(choices=[(True, 'Yes'), (False, 'No')], 
            validators=[InputRequired()],
            validate_choice=True or False)
    submit = SubmitField('Add the Task')

