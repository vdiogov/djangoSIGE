from django.contrib import admin
from .models import ProdutoEstocado, LocalEstoque

admin.site.register(ProdutoEstocado)
admin.site.register(LocalEstoque)