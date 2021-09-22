from django.contrib import admin
from .models import Pessoas


class PessoasAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')

admin.site.register(Pessoas, PessoasAdmin)
