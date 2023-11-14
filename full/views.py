from django.shortcuts import render

# Create your views here.
#Crea la vista de la pagina principal
def index(request):
    return render(request, 'index.html')

#Crea la vista de la pagina de acerca de
def acerca(request):
    return render(request, 'about.html')

#Crea la vista de la pagina de contacto
def contacto(request):
    return render(request, 'contact.html')