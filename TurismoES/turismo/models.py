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

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
    
class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

class Servicios(models.Model):
    id = models.IntegerField(primary_key=True)
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='media/%Y/%m/%d',null=True, blank=True,verbose_name='Imagen')
    descripcion = models.CharField(max_length=200, null=True)
