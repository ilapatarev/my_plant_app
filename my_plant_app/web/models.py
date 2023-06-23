from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
def first_letter_is_capital(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")

def only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    MIN_LEN=2
    username=models.CharField(max_length=10, null=False, blank=False, validators=[MinLengthValidator(2)])
    first_name=models.CharField(null=False, blank=False, max_length=20, validators=[first_letter_is_capital], verbose_name='First Name')
    last_name=models.CharField(null=False, blank=False, max_length=20, validators=[first_letter_is_capital], verbose_name='Last Name')
    profile_picture=models.URLField(null=True, blank=True)

class Plant(models.Model):
    OUTDOOR_PLANTS='Outdoor Plants'
    INDOOR_PLANTS='Indoor Plants'
    TYPE_CHOICES=(
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )
    plant_type=models.CharField(null=False, blank=False, max_length=14, choices=TYPE_CHOICES)
    name=models.CharField(max_length=20, null=False, blank=False, validators=[only_letters])
    image_url=models.URLField(null=False, blank=False)
    description=models.TextField(null=False, blank=False)
    price=models.FloatField(null=False, blank=False)