from django.contrib import admin

# Register your models here.
from pessoa.models import Pessoa

admin.site.register(Pessoa)