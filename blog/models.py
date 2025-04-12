from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #clave foránea de Tabla autor
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) #clave foránea de Tabla Categoría
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
