from django.contrib import admin

# Register your models here.
from outfit.web.models import Outfit, OutfitPhoto


class OutfitInlineAdmin(admin.StackedInline):
    model = Outfit


@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

@admin.register(OutfitPhoto)
class OutfitPhoto(admin.ModelAdmin):
    pass

