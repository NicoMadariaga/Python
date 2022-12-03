"""aprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

#Importar app con mis vistas
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),#la ruta la colocamos vacia xq queremos que index sea la pagina de inicio
    path('pagina/', views.pagina, name="pagina"),
    path('pagina/<int:redirigir>/', views.pagina, name="pagina"),
    #ara que sean parametro opcionales, debemos crear las rutas con todas las opciones posibles
    #En este caso es si no se pasa parametro o si si se pasa parametro
    path('contacto/', views.contacto, name="contacto"),#pasamos un dato como parametro
    path('contacto/<str:nombre>/', views.contacto, name="contacto"),#pasamos un dato como parametro
    path('editar-articulo/<int:id>/', views.editar_articulo),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulos/<int:id>/', views.borrar_articulo, name="borrar"),
    path('create-article/', views.create_article, name="create"),
    path('save-article/', views.save_article, name="save"),#url que se utiliza para guardar el articulo en la BD, no tiene template
    path('create-full-article/', views.create_full_article, name="creta_full_article"),
    path('buscar-articulo/', views.buscar_articulo, name="buscar"),
    path('articulo/', views.articulo, name="articulo")
]


#Configuracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)