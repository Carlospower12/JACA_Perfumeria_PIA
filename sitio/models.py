from django.db import models

class Perfume(models.Model):
    nombre = models.CharField(max_length=180)
    marca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=80)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to="perfumes/", blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.marca} - {self.nombre}"

class ArchivoSubido(models.Model):
    nombre = models.CharField(max_length=180)
    archivo = models.FileField(upload_to="archivos/")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
