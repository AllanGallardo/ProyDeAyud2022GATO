
from django import forms
from .models import Miembro
from .choices import POSITION_CHOICES
'''// create a select form field in django?
models.py:

    class MyModel(models.Model):
        field1 = models.CharField(max_length=40, blank=False, null=False)
        field2 = models.CharField(max_length=60, blank=True, null=True)

forms.py:

    class FormForMyModel(forms.Form):
        form_field1 = forms.CharField(max_length=40, required=True)
        form_field2 = forms.CharField(max_length=60, required=False)

views.py:

    def create_a_my_model(request):
        if request.method == 'POST':
            form = FormForMyModel(request.POST)
            if form.is_valid():
                my_model = MyModel()
                my_model.field1 = form.cleaned_data.get('form_field1', 'default1')
                my_model.field2 = form.cleaned_data.get('form_field2', 'default2')
                my_model.save()
        else:        
            form = FormForMyModel()
        context_data = {'form': form}
        return HttpResponse('templtate.html', context_data)


models.py:

    class MyModel(models.Model):
        field1 = models.CharField(max_length=40, blank=False, null=False)
        field2 = models.CharField(max_length=60, blank=True, null=True)

forms.py:

    class MyModelForm(forms.ModelForm):  # extending ModelForm, not Form as before
        class Meta:
            model = MyModel

views.py:

    def create_a_my_model(request):
        if request.method == 'POST':
            form = MyModelForm(request.POST)
            if form.is_valid():
                # save the model to database, directly from the form:
                my_model = form.save()  # reference to my_model is often not needed at all, a simple form.save() is ok
                # alternatively:
                # my_model = form.save(commit=False)  # create model, but don't save to database
                # my.model.something = whatever  # if I need to do something before saving it
                # my.model.save()
        else:        
            form = MyModelForm()
        context_data = {'form': form}
        return HttpResponse('templtate.html', context_data)
'''


class MemberForm(forms.ModelForm):
    class Meta: 
        # esta clase provee info adicional a la clase MemberForm
        model = Miembro # se define a cuál tabla pertenece este form
        fields = ('rut', 'nombre', 'nacionalidad', 'edad', 'dorsal', 'posicion') # se define que se mostrará en el form todos los atrbutos de la tabla
        ''' se puede utilizar __all__ para indicar que se quieren incluir en 
        el form todos los atributos '''
    # end class
    # falta crear un campo para ña posicion
    # este campo es especial porque es de tipo de selección
    '''posicion = forms.ChoiceField(choices= POSITION_CHOICES,
            widget=forms.Select())'''
# end class