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
    '''Función que obtiene los miembros con sus datos desde la base de datos
    y se los envía al archivo HTML correspondiente'''
    myMembers = Miembro.objects.all() # Consulta SQL, equivalente a select * from Miembro;
    context = {'members': myMembers}
    ''' La variable anterior corresponde al contexto de la página respectiva, este contexto
    es un diccionario y dentro de él se coloca toda la información que le queramos pasar al archivo HTML,
    en este caso estamos enviándole a la página list.html todos los datos de los miembros del equipo'''
    return render(request, 'team_register/list.html', context) # importante enviar el contexto

def agregar(request):
    '''Función que agrega un nuevo miembro al equipo'''
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
        return redirect('/team')
# end def

def eliminar(request, rut):
    ''' Función que dado un rut elimina el miembro del equipo correspondiente '''
    deleteMiembro = Miembro.objects.get(pk=rut) # equivalente a SQL Query SELECT * from Miembro WHERE rut = rut;
    deleteMiembro.delete() # se elimina de la base de datos
    return redirect('/team/list/') # se redirige a la página donde se muestra la lista de miembros
# end def

def editar(request, rut):
    '''Función que dado un rut despliega la información de dicho miembro
    para editarla y finalamente guardarla en la base de datos'''
    miembro = Miembro.objects.get(pk=rut) # se busca en la BD el miembro con el rut correspondiente
    if request.method == 'GET':
        # Usuario no ha ingresado info, se crea form con datos establecidos
        form = MemberForm(instance=miembro) # se pasa el miembro como parámetro para que se llene el form con los datos
        return render(request, 'team_register/editar-miembro.html', {'form': form})
    else:
        # POST, usuario editó los datos, se procesan y se guardan en la BD
        form = MemberForm(request.POST, instance=miembro) # actualizar form con nuevos datos
        if form.is_valid():
            form.save()
        return redirect('/team')
# end def
