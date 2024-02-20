from django.db import models

# Create your models here.

class Dane(models.Model):
    mass = models.FloatField(blank=True, null=True)
    feh = models.FloatField(blank=True, null=True)
    fov = models.FloatField(blank=True, null=True)
    model = models.FloatField(blank=True, null=True)
    logt = models.FloatField(blank=True, null=True)
    logl = models.FloatField(blank=True, null=True)
    pf = models.FloatField(blank=True, null=True)
    ef = models.FloatField(blank=True, null=True)
    p1 = models.FloatField(blank=True, null=True)
    e1 = models.FloatField(blank=True, null=True)
    p2 = models.FloatField(blank=True, null=True)
    e2 = models.FloatField(blank=True, null=True)
    p3 = models.FloatField(blank=True, null=True)
    e3 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dane'
