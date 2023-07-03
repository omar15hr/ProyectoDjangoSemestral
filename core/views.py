from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from .forms import *
import bcrypt
# Create your views here.
def root(request):
    return redirect('index')

def index(request):
    return render(request,'core/index.html')

def productos(request):
    mostrar_en_navbar = True
    return render(request,'core/productos.html', {'mostrar_en_navbar': mostrar_en_navbar})

def eventos(request):
    return render(request,'core/eventos.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def contacto(request):
    data = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado."
        else:
            data["form"] = formulario

    return render(request,'core/contacto.html', data)

def contacto_list(request):
    # formulario = Formulario.objects.all()
    # data = {
    #     'formulario' : formulario
    # }
    return render(request, 'core/contacto_list.html')

def register(request):
    if request.method == 'GET':
        return render(request,"core/register.html")
    else:
        if request.method == 'POST':
            errors = User.objects.validador_campos(request.POST)

            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value) 

                #Si se produce un error pero no queremos perder los datos....
                request.session['registro_nombre'] = request.POST['first_name']
                request.session['registro_apellido'] = request.POST['last_name']
                request.session['registro_email'] = request.POST['email']
                request.session['level_mensaje'] = 'alert-danger'

            else:
                request.session['registro_nombre'] = ""
                request.session['registro_apellido'] = ""
                request.session['registro_email'] = ""

                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

                obj = User.objects.create(first_name=first_name, last_name=last_name,email=email,password=password_hash)
                messages.success(request, "Usuario registrado con éxito!!!!")
                request.session['level_mensaje'] = 'alert-success'
            
            return redirect('core/register.html')

        return render(request, 'core/register.html')

def login(request):
    if request.method == 'GET':
        return render(request,"core/login.html")
    else:
        if request.method == 'POST':
            
            user = User.objects.filter(email=request.POST['email_login']) #Buscamos el correo ingresado en la BD             
            
            if user : #Si el usuario existe

                usuario_registrado = user[0]
                
                if bcrypt.checkpw(request.POST['password_login'].encode(), usuario_registrado.password.encode()): 
                    usuario = {
                        'id':usuario_registrado.id,
                        'first_name':usuario_registrado.first_name,
                        'last_name':usuario_registrado.last_name,
                        'email':usuario_registrado.email,
                        'rol':usuario_registrado.rol,
                    }

                    request.session['usuario'] = usuario
                    messages.success(request,"Ingreso correcto!!!!")
                    return redirect('/index')
                else:
                    messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                    return redirect('/')
            else:
                messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                return redirect('/')
            
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return redirect('/')