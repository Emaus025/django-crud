from django.db import models
from django.contrib.auth.models import User

class Partitura(models.Model):
    DIFICULTAD_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    VISIBILIDAD_CHOICES = [
        ('publica', 'Pública'),
        ('privada', 'Privada'),
    ]

    titulo = models.CharField(max_length=255, verbose_name="Título")
    compositor = models.CharField(max_length=255, verbose_name="Compositor")
    arreglista = models.CharField(max_length=255, blank=True, null=True, verbose_name="Arreglista")
    genero = models.CharField(max_length=100, verbose_name="Género")
    instrumentos = models.CharField(max_length=255, verbose_name="Instrumentos")
    dificultad = models.CharField(max_length=50, choices=DIFICULTAD_CHOICES, verbose_name="Dificultad")
    archivo = models.FileField(upload_to='partituras/', verbose_name="Archivo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    visibilidad = models.CharField(max_length=50, choices=VISIBILIDAD_CHOICES, default='publica', verbose_name="Visibilidad")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Partitura"
        verbose_name_plural = "Partituras"