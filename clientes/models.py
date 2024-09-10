from django.db import models


# Se crea la clase/modelo ciudad con los atributos de cada una de ellas
class ciudad(models.Model):
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.ciudad} {self.codigo_postal}"

# Se crea la clase/modelo lugar con los atributos de cada una de ellas
class lugar(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.direccion} {self.comuna}"

# Se crea la clase/modelo "producto" con los atributos de cada una de ellas
class producto(models.Model):
    Nombre_producto = models.CharField(max_length=50)
    Codigo_producto = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.Nombre_producto} {self.Codigo_producto} {self.Categoria}"
    