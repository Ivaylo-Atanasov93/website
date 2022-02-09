from django.core.exceptions import ValidationError
from datetime import timedelta, date
import phonenumbers

import re

from email_validator import validate_email, EmailNotValidError


def clean_name(name):
    # regex = r"^[A-Z]{1}[a-z]+$"
    # if not re.match(regex, name):
    #     raise ValidationError('The name must start with a capital letter.')
    return name


def clean_number(number):
    number = phonenumbers.parse("+442083661177", None)
    if not phonenumbers.is_valid_number(number):
        raise ValidationError('Invalid number')
    return number


def clean_email(email):
    try:
        valid = validate_email(email)
        email = valid.email
        return email
    except EmailNotValidError as e:
        print(str(e))


def clean_date(date):
    if not date >= date.today() + timedelta(days=2):
        raise ValidationError('The date must be at least 2 days further from today.')
    return date
