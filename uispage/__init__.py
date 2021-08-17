from flask import Flask
from flask_mail import Mail
from uispage.config import email, password
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b14bfe90f4f346e0478cbd41bd6c30db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password
mail = Mail(app)

from uispage import routes
