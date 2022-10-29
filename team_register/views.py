from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Miembro
# Create your views here.

'''Aquí irán las funciones que desempeñarán la lógica 
    de la aplicación, por cada url hay una función y una plantilla html,
    además estas  funciones son el nexo entre la base de datos 
    y el front end '''

def index(request):
    # home page para nuestro sitio
    return render(request, 'team_register/index.html')
    '''la función render le envía al navegador 
    la correspondiente plantilla html'''
# end  def

def listar(request):
    return render(request, 'team_register/list.html')

def agregar(request):
    if request.method == "GET":
        # Usuario no ha ingresado info, se crea form vacío
        form = MemberForm() # instancia de un form para Miembro
        return render(request, "team_register/nuevo-miembro.html", {'form': form});
    else:
        # Usuario ya ingresó info, se procesa dicha info
        # el método en este caso es POST
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save() # se guarda info en la base de datos
        return redirect('/team/')
# end def