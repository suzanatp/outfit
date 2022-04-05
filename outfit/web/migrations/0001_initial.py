# Generated by Django 4.0.3 on 2022-04-03 14:25

import django.core.validators
from django.db import migrations, models
import outfit.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), outfit.common.validators.validator_only_letters])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), outfit.common.validators.validator_only_letters])),
                ('image', models.URLField()),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], default='Do not show', max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
