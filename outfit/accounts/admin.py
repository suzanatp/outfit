from django.contrib import admin

from outfit.accounts.models import Profile, OutfitUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(OutfitUser)
class RegisterAuthUser(admin.ModelAdmin):
    pass
