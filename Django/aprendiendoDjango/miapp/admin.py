from django.contrib import admin
from miapp.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=("id", "title", "public", "create_at")
    search_fields=("id","title")#Ingresamos los campos por los cual queremos q se busque
    list_filter=("create_at",)
    date_hierarchy=("create_at")

# Register your models here.
admin.site.register(Article, ArticleAdmin)

# Cambiar el Encabezado
admin.site.site_header = 'Aprendiendo Django'

#Cambiamos el titulo
admin.site.site_title = 'Nicolas Madariaga'
admin.site.index_title = 'Estoy aprendiendo'