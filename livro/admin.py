from django.contrib import admin
from .models import Livros, Emprestimos

# Register your models here.

admin.site.register(Livros)
admin.site.register(Emprestimos)
