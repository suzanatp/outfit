from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from outfit.web.validators import validator_only_letters


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 0

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validator_only_letters,
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validator_only_letters,
        ]
    )
    image = models.URLField()

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
