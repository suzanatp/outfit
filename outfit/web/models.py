from django.contrib.auth import get_user_model

from django.db import models

from outfit.accounts.models import OutfitUser

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

    SUNNY = "Sunny"
    WINDY = "Windy"
    RAINY = "Rainy"
    SNOW = "Snow"
    NOT_AVAILABLE = "N/A"
    # STORMY = "Stormy"

    TYPES = [(x, x) for x in (SUNNY, WINDY, RAINY, SNOW, NOT_AVAILABLE)]
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

    weather = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
        default=NOT_AVAILABLE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}"

    @property
    def comments_count(self):
        return self.comment_set.count()

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
    #
    # likes = models.IntegerField(
    #     default=0,
    # )
    # dislikes = models.IntegerField(
    #     default=0,
    # )
    price = models.CharField(
        max_length=max(len(x) for (x, _) in PRICES),
        choices=PRICES,
    )

    outfit_id = models.ForeignKey(
        Outfit,
        verbose_name="Outfit",
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def likes_count(self):
        return self.like_set.count()

    @property
    def dislikes_count(self):
        counts = self.dislike_set.count()
        return int(counts) * (-1)


class Like(models.Model):
    photo = models.ForeignKey(
        OutfitPhoto,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Dislike(models.Model):
    photo = models.ForeignKey(
        OutfitPhoto,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    TEXT_MAX_LENGTH = 300
    text = models.TextField(
        max_length=TEXT_MAX_LENGTH,
    )
    outfit = models.ForeignKey(
        Outfit,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    time = models.DateTimeField(
        auto_now_add=True,
    )
