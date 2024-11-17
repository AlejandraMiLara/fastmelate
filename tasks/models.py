from django.db import models
from django.contrib.auth.models import User

class NumeroSorteo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()
    r6 = models.IntegerField()
    fecha_generado = models.DateField(auto_now_add=True)
    hora_generado = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.r1}, {self.r2}, {self.r3}, {self.r4}, {self.r5}, {self.r6}"
