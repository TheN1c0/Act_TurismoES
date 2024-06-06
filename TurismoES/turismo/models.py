from django.db import models

# Create your models here.
""" Clase creada por la importación de una clase
para tomar como modelo, nombre imagen y dirección """
class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    """ Instancia del objeto interpretada como cadena """
    def __str__(self):
        return self.title