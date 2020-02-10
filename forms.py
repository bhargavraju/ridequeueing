from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class RideCreationForm(FlaskForm):
    customer_id = IntegerField('Customer Id', validators=[DataRequired()])
    submit = SubmitField('Create Ride')
