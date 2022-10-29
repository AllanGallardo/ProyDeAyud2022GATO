
from dataclasses import field
from random import choices
from secrets import choice
from django.db import models 
from .choices import POSITION_CHOICES

'''class Profile(models.Model):

    customer_username = models.CharField(max_length=100)
    customer_email = models.EmailField()


import uuid

class Profile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    customer_username = models.CharField(max_length=100)
    customer_email = models.EmailField()'''
'''STATUS_CHOICES = (
    (1, _("Not relevant")),
    (2, _("Review")),
    (3, _("Maybe relevant")),
    (4, _("Relevant")),
    (5, _("Leading candidate"))
)
RELEVANCE_CHOICES = (
    (1, _("Unread")),
    (2, _("Read"))
)


from myApp.choices import * 

class Profile(models.Model):
    user = models.OneToOneField(User)    
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)   
    relevance = models.IntegerField(choices=RELEVANCE_CHOICES, default=1)


from myApp.choices import * 

class CViewerForm(forms.Form):

    status = forms.ChoiceField(choices = STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    relevance = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)
'''






# Create your models here.
# Cada clase representará una tabla en la base de datos

#end class
class Miembro(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    nacionalidad = models.CharField(max_length=50, null=False)
    edad = models.IntegerField(null=False)
    dorsal = models.IntegerField(null=True, blank=True)
    '''a continuación FK de la tabla Posicion'''
    posicion = models.CharField(max_length=40,
        choices=POSITION_CHOICES, default='PO')

    ''' Aquí simplemente se definió una tabla con sus atributos 
    por ejemplo el nombre en la base de datos se traducirá a 
    nombre varchar(50);'''
# end class
