from django.core.validators import RegexValidator
from django.db import models
import re
from django.core.exceptions import ValidationError

def validate_password(value):
    if not re.findall(r'[A-Z]', value):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not re.findall(r'[a-z]', value):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not re.findall(r'[0-9]', value):
        raise ValidationError('Password must contain at least one number.')
    if not re.findall(r'[\W_]', value):
        raise ValidationError('Password must contain at least one symbol.')

class User(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
            message='Enter a valid email address.',
        )
    ])
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=50, validators=[validate_password])
    confirm_password = models.CharField(max_length=50)
    user_role = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname