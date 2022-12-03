from django import forms
    
class FormArticle(forms.Form):
    
    #Definimos las propiedades, o sea los campos que va a contener este formulario
    #Campo de tipo texto
    title = forms.CharField( label="Titulo")
    #Campo de tipo Textarea
    content = forms.CharField(label="Contenido", widget=forms.Textarea)

    #creamos un campo select
    #cremos al variable para las opciones
    public_options = [(1, "Si"), (0, "No")]
    public = forms.TypedChoiceField(
        label = "¿Publico?",
        choices = public_options 
    )

