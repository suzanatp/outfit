from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from outfit.common.validators import validator_only_letters

UserModel = get_user_model()


class Outfit(models.Model):
    CASUAL = "Casual"
    VINTAGE = "Vintage"
    BOHEMIAN = "Bohemian"
    TRENDY = "Trendy"
    ELEGANT = "Elegant"
    SPORTY = "Sporty"

    WINTER = "Winter"
    SPRING = "Spring"
    SUMMER = "Summer"
    AUTUMN = "Autumn"

    CATEGORIES = [(x, x) for x in (CASUAL, VINTAGE, BOHEMIAN, TRENDY, ELEGANT, SPORTY)]
    SEASONS = [(x, x) for x in (WINTER, SPRING, SUMMER, AUTUMN)]
    NAME_MAX_LENGTH = 15

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    category = models.CharField(
        max_length=max(len(x) for (x, _) in CATEGORIES),
        choices=CATEGORIES,
    )

    season = models.CharField(
        max_length=max(len(x) for (x, _) in SEASONS),
        choices=SEASONS,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user', 'name')


class OutfitPhoto(models.Model):
    INEXPENSIVE = "$"
    MODERATELY_EXPENSIVE = "$$"
    EXPENSIVE = "$$$"
    VERY_EXPENSIVE = "$$$$"

    PRICES = [(x, x) for x in (INEXPENSIVE, MODERATELY_EXPENSIVE, EXPENSIVE, VERY_EXPENSIVE)]

    photo = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )
    price = models.CharField(
        max_length=max(len(x) for (x, _) in PRICES),
        choices=PRICES,
    )

    outfit_id = models.ForeignKey(
        Outfit,
        on_delete=models.CASCADE,
    )

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )


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


# class Event(models.Model):
#     MAX_LENGTH_TITLE = 15
#
#     title = models.CharField(
#         max_length=MAX_LENGTH_TITLE,
#     )
#
#     date = models.DateTimeField()
#
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#


