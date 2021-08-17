from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, TextAreaField
from wtforms import validators
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo, NumberRange

class GradesForm(FlaskForm):
    grade1 = DecimalField('Grade 1',
                        validators=[InputRequired(), NumberRange(min=0, max=5)], default=0)
    grade2 = DecimalField('Grade 2',
                        validators=[InputRequired(), NumberRange(min=0, max=5)], default=0)
    grade3 = DecimalField('Grade 3',
                        validators=[InputRequired(), NumberRange(min=0, max=5)], default=0)
    grade4 = DecimalField('Grade 4',
                        validators=[InputRequired(), NumberRange(min=0, max=5)], default=0)
    grade5 = DecimalField('Grade 5',
                        validators=[InputRequired(), NumberRange(min=0, max=5)], default=0)
    grade6 = DecimalField('Grade 6',
                        validators=[InputRequired(), NumberRange(min=0, max=5)], default=0)
    percentage1 = DecimalField('Percentage 1',
                        validators=[InputRequired(), NumberRange(min=0, max=100)], default=0)
    percentage2 = DecimalField('Percentage 2',
                        validators=[InputRequired(), NumberRange(min=0, max=100)], default=0)
    percentage3 = DecimalField('Percentage 3',
                        validators=[InputRequired(), NumberRange(min=0, max=100)], default=0)
    percentage4 = DecimalField('Percentage 4',
                        validators=[InputRequired(), NumberRange(min=0, max=100)], default=0)
    percentage5 = DecimalField('Percentage 5',
                        validators=[InputRequired(), NumberRange(min=0, max=100)], default=0)
    percentage6 = DecimalField('Percentage 6',
                        validators=[InputRequired(), NumberRange(min=0, max=100)], default=0)                      
    submit = SubmitField('Check')


class ContactForm(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired(), Length(min=2)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    subject = StringField('Subject',
                        validators=[DataRequired()])
    information = TextAreaField('Information',
                        validators=[DataRequired()])    
    submit = SubmitField('Submit')