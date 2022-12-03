from django import template

#Creamos una variable para cargar la libreria de template
register = template.Library()

#Creamos el registro
@register.filter(name='saludo')
def saludo(value):
    return f"<h1 style='background:green;color:white;'>Bienvenido {value}</h1>"