# -*- coding: utf-8 -*-

from django.db import models
import datetime

class Categoria(models.Model):
    categoria_name = models.CharField(max_length=50)

class TipoTerapia(models.Model):
    nombre = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    costoUnitario = models.FloatField()

class Terapia(models.Model):
    tipo = models.ForeignKey(TipoTerapia, on_delete=models.CASCADE)
    fecha_creada = models.DateField("fecha de creación de la terapia")
    fecha_programada = models.DateField("fecha de ejecución de la terapia")

