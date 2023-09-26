from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def login(request):
    #Key: value
    context= { 'nombre':'Top Games' }
    # Lógica para la página de inicio de sesión
    return render(request, 'core/login.html', context)

def contacto(request):
    # Lógica para la página de contacto
    return render(request, 'core/contacto.html')



def categoria_carreras(request):
    # Lógica para la página de contacto
    return render(request, 'core/categoria/carreras.html')

def categoria_deporte(request):
    # Lógica para la página de contacto
    return render(request, 'core/categoria/deporte.html')

def categoria_lucha(request):
    # Lógica para la página de contacto
    return render(request, 'core/categoria/lucha.html')

def categoria_terror(request):
    # Lógica para la página de contacto
    return render(request, 'core/categoria/terror.html')

def categoria_accion(request):
    # Lógica para la página de contacto
    return render(request, 'core/categoria/accion.html')

def categoria_shooter(request):
    # Lógica para la página de contacto
    return render(request, 'core/categoria/shooter.html')


 # JUEGOS
def juego_accion1(request):
    # Lógica para la página de contacto
    return render(request, 'core/juego/juego_accion1.html')



#def juego_show(request, id):
    # Lógica para la página de contacto
    #juegos = ['accion1', 'accion2', 'accion3']
    #images = ['accion1.jpg', 'accion2.jpg', 'accion3.jpg']
    #juego = juegos ['id-1']
    #img = images ['id-1']

    #context= { 
       # 'nombre':juego,
        #'img':img
        #}
   # return render(request, 'core/juego/show.html', context)



def juego_show(request, id):
    # Lógica para la página de contacto
    juegos = ['accion1', 'accion2', 'accion3']
    images = ['accion1.jpg', 'accion2.jpg', 'accion3.jpg']
    juego = juegos[int(id) - 1]
    img = images[int(id) - 1]

    context = { 
        'juego': juego,  # Cambiado de 'nombre' a 'juego'
        'img': img
    }
    return render(request, 'core/juego/show.html', context)





