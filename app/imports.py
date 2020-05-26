from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL
from flask_wtf import RecaptchaField
import uuid