from django.db import models


class productos(models.Model):
    clave_producto = models.CharField(
        max_length=20, blank=False, primary_key=True)
    nombre_producto = models.CharField(max_length=50, blank=False)
    categoria_producto = models.CharField(max_length=50, blank=True)
    catidad_producto = models.IntegerField(blank=False)
    catidad_reserva_producto = models.IntegerField(blank=False)
    precio_compra_producto = models.IntegerField(blank=False)
    precio_venta_producto = models.IntegerField(blank=False)
    fecha_caducidad_producto = models.DateField(null=True)
    informacion_producto = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return "%s" % (self.productos)

    class Meta:
        db_table = "productos"


class categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return "%s" % (self.categorias)

    class Meta:
        db_table = "categorias"
