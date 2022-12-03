from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here

def index(request):
    
    nombre = "Nico Madariaga"
    lenuajes = ['JavaScript', 'Python', 'Java', 'PHP']
    #Pasamos como parametro un diccionario con las variabales
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenuajes
    })
    #return HttpResponse(layout+html)

def pagina(request):

    return render(request, 'pagina.html')

def contacto(request):
    return render(request, 'contacto.html')


def save_article(request):
    #comprobamos si el request que recibimos tiene algun elemento
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse(f"Articulo cargado: {articulo.title} - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el artiiculo</h2>")

def create_article(request):
    return render(request,'create_article.html')

#Vista para mostrar el formulario en base a clase FormArticle
def create_full_article(request):
    
    #Confirmamos si nos llega informacion por el POST
    if request.method == 'POST':
        #Creamos un formulario con los datos del post
        formulario = FormArticle(request.POST)

        #Corroboramos si el formaulario es valido
        if formulario.is_valid():
            #Creamos una variable con los datos del formulario
            date_form = formulario.cleaned_data

            title = date_form['title']
            content = date_form['content']
            public = date_form['public']

            #Creamos el articulo y lo guardamos en la base de datos, este codigo podria ser una funcion tb
            articulo = Article(
            title = title,
            content = content,
            public = public
            )
            articulo.save()

            #Crear mensaje flash, elegimos el tipo de mensaje q ue queremos mostrar
            # en este caso es un succes, puede ser un error tb
            messages.success(request, f'Has creado correctamente el articulo {articulo.title}')

            return redirect('articulos')

    else: #Si el mensaje esta vacío, devolvemos un formulario vacio
        #llamamos al formulario creando una variable
        formulario = FormArticle()

    #retornamos la url, y pasamos el formulario como parametro
    return render(request, 'create_full_article.html', {'form':formulario})

def buscar_articulo(request):
    return render(request,'buscar_articulo.html')
#Vista para obtener los elementos de la base de datos con los modelos

def articulo(request):
    #creamos un objeto articulo para obtener un registro de la base de datos
    #en el metodo POST, se puede buscar con los distintos atributos
    
    if request.method == 'POST':
        title = request.POST['title']
        articulo = Article.objects.get(title=title)

        return HttpResponse(f"<strong> El articulo obteniido es: {title} </strong>")
        #return HttpResponse(f"<strong> El articulo obteniido es: {articulo.title} </strong>")
    else:
        return HttpResponse("<h2>No se ha podido crear el artiiculo</h2>")

#Vista para modificar un articulo, le pasamos el id como parametro
def editar_articulo(request, id):
    articulo = Article.objects.POST(id=id)

    #Modificamos los atributos que necesitamos
    articulo.title = "Titulo modificado"
    articulo.content = "Contenido modificado"

    #guardamos los cambios
    articulo.save()
    
    return HttpResponse(f"<strong> El articulo modificado es: {articulo.title} - {articulo.content} </strong>")

#Vista para mostrar todos los articulos de la tabla
def articulos(request):
    #El metodo all(),  obtiene todos los articulos de la tabla
    articulos = Article.objects.filter(public=True)
    #El metodo order_by()obtiene los datos ordenados por el parametro que le indiquemos
    #si al parametro lo colocamo con un -, los ordena de forma descendente
    #articulos = Article.objects.order_by('title')
    #articulos = Article.objects.filter(id=2)
    #Filter, filtra la consulta por el o los parametros que se le pasa
    #articulos = Article.objects.raw("SELECT * FROM miapp_article")

    return render(request, 'articulos.html', {'articulos': articulos})

def borrar_articulo(request, id):
    articulo = Article.objects.get(id=id)
    articulo.delete()

    return redirect('articulos')