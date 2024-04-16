from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in basket
class CheckoutForm(FlaskForm):
    firstname = StringField("Your Firstname",validators=[InputRequired()])
    surname = StringField("Your Surname", validators=[InputRequired()])
    email = StringField("Your Email", validators=[InputRequired(), email()])
    phone = StringField("Your Phone Number", validators=[InputRequired()])
    submit = SubmitField("Send to Agent")