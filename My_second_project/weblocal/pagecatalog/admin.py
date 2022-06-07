from django.contrib import admin

# Register your models here.
from .models import Genre,Language,Producer,Film,FilmOrder,Actor


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Producer)

class FilmOrderInline(admin.TabularInline):
    model = FilmOrder

    def __str__(self):
        return f"{self.model.film}, {self.model.status}, {self.model.was_watched}, {self.model.id}"

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title","actor","display_genre")

    inlines = [FilmOrderInline]

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","date_of_birth","date_of_death")


@admin.register(FilmOrder)
class FilmOrderAdmin(admin.ModelAdmin):
    list_display = ("film","status","was_watched")
    list_filter = ("status","was_watched")

    fieldsets = (
        (None, {
            'fields': ('film','imprint','id')
        }),
        ("Availability", {
            'fields': ('status','was_watched')
        }),
    )
