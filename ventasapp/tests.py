from django.test import TestCase
from .models import Venta

class VentaTestCase(TestCase):
    def setUp(self):
        Venta.objects.create(fecha="2023-01-01", concepto="Venta de prueba", cantidad=10, precio=5.00)

    def test_venta_total(self):
        venta = Venta.objects.get(concepto="Venta de prueba")
        self.assertEqual(venta.total, 50.00)
