from django.db import models
from django.conf import settings

class Venta(models.Model):
    producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto} - {self.cantidad} - {self.precio}'




    def ingreso_total(self):
        return self.cantidad * self.precio

    def ganancia_28(self):
        return self.ingreso_total() * 0.28

    def ganancia_14(self):
        return self.ingreso_total() * 0.14

    def publicidad(self):
        return self.ingreso_total() * 0.10

    def inversion(self):
        return self.ingreso_total() * 0.20

    def diezmo(self):
        return self.ingreso_total() * 0.10

    def ofrenda(self):
        return self.ingreso_total() * 0.05
