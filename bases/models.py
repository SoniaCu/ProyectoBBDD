 ## importacion de django por defecto
from django.db import models

#modelo de usuario que trae django
from django.contrib.auth.models import User 

# creacion de claseModelo y hereda de models.Model
# crear las tablas de las pripiedades que se repiten en los modelos
# se utilizan propiedad de tipo field porque luego se van a migrar a la bd

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)     # valor por defecto true
    fc = models.DateTimeField(auto_now_add=True)   #fechacreacion registrar hora y fecha del servidor
    fm = models.DateTimeField(auto_now=True)       #fechamodifica de tipo models cuando se inserta coloca la fecha y cuando se modifica tambien
    uc = models.ForeignKey(User, on_delete=models.CASCADE)   #usuarioquecrea en esta parte se importa el modelo de usuario que trae django, 
                                                              # será de tipo foreinKey al modelos user para guardar cada uno de los usuarios con relacion de uno a muchos porque un usuario va estar en muchos modelos
    
    um = models.IntegerField(blank=True, null=True)   #usuariomodifica

    # para que django no lo tome en cuenta al hacer la migracion
    class Meta:
        abstract=True 

