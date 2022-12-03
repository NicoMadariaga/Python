from django.db import models

# Create your models here.
#Creamos un modelo.
class Article(models.Model):
    #definimos las variables y su tipo
    title = models.CharField(max_length=150)#Varchar
    content = models.TextField(verbose_name="contenido")#Texto
    #Colocamos esta variable como ejemplom para la modificacion
    image = models.ImageField(default='null', upload_to='articles')
    public = models.BooleanField()#Booleano
    create_at = models.DateTimeField(auto_now_add=True)#Fecha, y el auto hace que nos gusrde automaticamente la fecha de creacion
    update_at = models.DateTimeField(auto_now=True)

    #Para modificar la forma en que nos muestra los registros en el Panel de Control
    def __str__(self):
        return f"Id: {self.id}, Titulo: {self.title}"
    

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()