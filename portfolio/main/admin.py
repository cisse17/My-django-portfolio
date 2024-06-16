from django.contrib import admin
from .models import Tag, ProjetImage, Projet

# Register your models here.

class ProjetImageInline(admin.TabularInline):
    model = ProjetImage
    extra = 1

class ProjetAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "lien"
    )
    inlines = [ProjetImageInline]
    search_fields = ("titre", "description")
    list_filter = ("tags", )

class TagAdmin(admin.ModelAdmin):
    list_display = ("nom", )
    search_fields = ("nom",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(ProjetImage)

